import boto3
import os
srcKey = str(os.environ.get('FILE'))
videoName = str(os.environ.get('FILE'))
srcBucket = str(os.environ.get('BUCKET'))
videoName = videoName.rsplit("/",2)[1]
uploadKeyName = srcKey.rsplit("/",1)[0] + "/Azure_Results.csv"
resource = boto3.resource('s3')
resultFileName = '/tmp/Azure_' + videoName + '_result.csv'
resource.meta.client.upload_file("%s"%resultFileName,srcBucket,uploadKeyName)
