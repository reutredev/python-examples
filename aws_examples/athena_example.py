import time
import boto3
import pandas as pd
import io

listOfStatus = ['SUCCEEDED', 'FAILED', 'CANCELLED']
listOfInitialStatus = ['RUNNING', 'QUEUED']


class AthenaData:
    def __init__(self, db_name, bucket, folder):
        self.client = boto3.client("athena")
        self.db_name = db_name
        self.bucket = bucket
        self.folder = folder
        self.output_location = 's3://' + self.bucket + '/' + self.folder

    def start_query(self, query):
        response = self.client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={"Database": self.db_name},
            ResultConfiguration={"OutputLocation": self.output_location}
        )

        return response["QueryExecutionId"]

    def process_query_till_finish(self, execution_id: str) -> bool:
        query_status = 'QUEUED'
        try:
            while query_status in listOfInitialStatus:
                query_status = \
                    self.client.get_query_execution(QueryExecutionId=execution_id)['QueryExecution']['Status']['State']
                print(query_status)
                if query_status == 'FAILED' or query_status == 'CANCELLED':
                    raise Exception(f'Athena query with the execution_id {execution_id} '
                                    f'failed or was cancelled')
                time.sleep(0.2)
            print('Query "{}" finished.'.format(execution_id))

            return True

        except Exception as e:
            print(e)
            return False

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


    # def get_query_results(self, execution_id):
    #     #     response = self.client.get_query_results(
    #     #         QueryExecutionId=execution_id
    #     #     )
    #     #
    #     #     results = response['ResultSet']['Rows']
    #     #     return results


def main():
    athena_data = AthenaData("customers_database", "reutre-athena-results", "customers_queries/")
    query = f'SELECT "customerid", "namestyle", "title", "firstname", "lastname", "emailaddress" ' \
            f'FROM customers_csv limit 10;'
    query2 = f'SELECT "customerid", "namestyle", "title", "firstname", "lastname", "emailaddress" ' \
            f'FROM customers_csv limit 20;'

    queries = [query, query2]
    time_before = time.perf_counter()
    for query in queries:
        execution_id = athena_data.start_query(query)
        print(f"execution id: {execution_id}")
        if athena_data.process_query_till_finish(execution_id):
            df = athena_data.obtain_data(execution_id)
            print(df.to_string())

    print(f"Total time (asynchronous): {time.perf_counter() - time_before}")


if __name__ == "__main__":
    main()
