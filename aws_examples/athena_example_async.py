import time
import boto3
import pandas as pd
import io
import asyncio

listOfStatus = ['SUCCEEDED', 'FAILED', 'CANCELLED']
listOfInitialStatus = ['RUNNING', 'QUEUED']


class AthenaData:
    def __init__(self, db_name, bucket, folder):
        self.client = boto3.client("athena")
        self.db_name = db_name
        self.bucket = bucket
        self.folder = folder
        self.output_location = 's3://' + self.bucket + '/' + self.folder

    async def process_query_till_finish(self, query: str):
        try:
            execution_id = await asyncio.to_thread(self.run_query_sync, query)
            print('Query "{}" finished.'.format(execution_id))

            return True, execution_id

        except Exception as e:
            print(e)
            return False, None

    def run_query_sync(self, query):
        response = self.client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={"Database": self.db_name},
            ResultConfiguration={"OutputLocation": self.output_location}
        )
        execution_id = response["QueryExecutionId"]
        query_status = 'QUEUED'
        while query_status in listOfInitialStatus:
            query_status = \
                self.client.get_query_execution(QueryExecutionId=execution_id)['QueryExecution']['Status']['State']
            print(execution_id, query_status)
            if query_status == 'FAILED' or query_status == 'CANCELLED':
                raise Exception(f'Athena query with the execution_id {execution_id} '
                                f'failed or was cancelled')
            time.sleep(0.2)

        return execution_id

    def obtain_data(self, execution_id: str) -> pd.DataFrame:
        try:
            s3_resource = boto3.resource('s3')

            response = s3_resource \
                .Bucket(self.bucket) \
                .Object(key=self.folder + execution_id + '.csv') \
                .get()

            return pd.read_csv(io.BytesIO(response['Body'].read()), encoding='utf8')

            # s3 = boto3.resource('s3')
            # obj = s3.Object('my-bucket', 'my-folder/{}.csv'.format(query_execution_id))
            # body = obj.get()['Body'].read()
            #
            # df = pd.read_csv(pa.BufferReader(body), encoding='utf8')
        except Exception as e:
            print(e)

    async def async_obtain_data(self, execution_id: str):
        return await asyncio.to_thread(self.obtain_data, execution_id)


async def main_async():
    athena_data = AthenaData("customers_database", "reutre-athena-results", "customers_queries/")
    query1 = f'SELECT "customerid", "namestyle", "title", "firstname", "lastname", "emailaddress" ' \
            f'FROM customers_csv limit 10;'
    query2 = f'SELECT "customerid", "namestyle", "title", "firstname", "lastname", "emailaddress" ' \
             f'FROM customers_csv limit 20;'

    queries = [query1, query2]
    print(f"started at {time.strftime('%X')}")
    time_before = time.perf_counter()

    tasks = []
    for query in queries:
        tasks.append(asyncio.create_task(athena_data.process_query_till_finish(query)))

    # Wait until both tasks are completed
    results = await asyncio.gather(*tasks)

    executions_to_read = [res[1] for res in results if res[0]]

    tasks_df = []
    for execution in executions_to_read:
        tasks_df.append(asyncio.create_task(athena_data.async_obtain_data(execution)))

    dfs = await asyncio.gather(*tasks_df)
    for df in dfs:
        print(df.to_string())
    print(f"finished at {time.strftime('%X')}")
    print(f"Total time (asynchronous): {time.perf_counter() - time_before}")

if __name__ == "__main__":
    asyncio.run(main_async())
