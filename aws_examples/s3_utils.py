import boto3


class S3Utils:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        # self.region = "eu-west-1"
        self.s3 = boto3.client('s3')

    def list_files(self, bucket_key):
        # s3 = boto3.client('s3', region_name=self.region)
        rsp = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=bucket_key)
        # ref_list_org = [f'{obj["Key"]}' for obj in rsp["Contents"] if (obj["Key"].endswith("/") is True)]
        ref_list_org = [f'{obj["Key"]}' for obj in rsp["Contents"] if obj["Key"].endswith("/") is False]
        print(ref_list_org)
        file_names = []
        for item in ref_list_org:
            file_name = item.split("/")[1]
            file_names.append(file_name)
        print(file_names)

    # def get_s3_object(self, object_name):
    #     s3_object = self.s3.get_object(Bucket=self.bucket_name, key=object_name)
    #     print(s3_object)

    def list_items(self):
        for key in self.s3.list_objects(Bucket=self.bucket_name)['Contents']:
            print(key['Key'])


if __name__ == "__main__":
    s3Utils = S3Utils("reutre-test1")
    s3Utils.list_files("testfiles/")
    s3Utils.list_items()
    #s3Utils.get_s3_object("testfiles/test_file1.txt")
