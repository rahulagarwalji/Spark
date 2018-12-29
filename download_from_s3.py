bucketName = "Your S3 BucketName"
Key = "Original Name and type of the file you want to upload into s3"
outPutname = "Output file name(The name you want to give to the file after we upload to s3)"

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)