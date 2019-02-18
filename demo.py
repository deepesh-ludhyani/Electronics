import boto3
bucketName='rohanmaheshwari9-test'
x=1
while x<=4:
    Key=f"photo{x}.jpg"
    outPutname=f"photo{x}.jpg"
    s3=boto3.client('s3')
    x+=1
    s3.upload_file(Key,bucketName,outPutname)
