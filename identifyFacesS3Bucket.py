import chaqer
from chaqer import Chaqer
import boto3
import os
import datetime
import pandas as pd
import numpy as np
import zipfile
chaqerObject = Chaqer()
s3 = boto3.resource('s3')
client = boto3.client('s3')
srcBucket = str(os.environ.get('BUCKET'))
srcKey = str(os.environ.get('FILE'))
# result = client.list_objects(Bucket = 'cloudarch-terraform')
# print result

Chuck=0
Shaq=0
colNames = ['Name','TimeStamp','ISO','Shaq','Chuck']
df = pd.DataFrame(columns=colNames)


localFilename = '/tmp/{}'.format(os.path.basename(srcKey))
try:
    s3.Bucket(srcBucket).download_file(srcKey, localFilename)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

zip_ref = zipfile.ZipFile(localFilename, 'r')
zip_ref.extractall('/tmp/')
zip_ref.close()

videoName = str(os.environ.get('FILE'))
videoName = videoName.rsplit("/",2)[1]


for imgFile in sorted(os.listdir('/tmp/')):
    if imgFile.find("img") != -1:
        #img = str(f.key)
        mili = '000'
        img = '/tmp/'+imgFile
        #print img
        ID = os.path.basename(imgFile)
        time = ID.split("_",1)[0]
        time = float(time)
        ISO = str(datetime.timedelta(seconds=time))
        strTime = ISO.rsplit(".",1)[0]
        try:
            mili = ISO.rsplit(".",1)[1]
            mili = mili[:-3]
        except:
            pass
        ISO = strTime+":"+mili
        #print timeStamp
        faceMatches = chaqerObject.identifyFacesS3('chaqer',img)
        for i in range(0,len(faceMatches)):
            if 'Chuck' in faceMatches[i]["Name"]:
                Chuck = 1
            elif 'Shaq' in faceMatches[i]["Name"]:
                Shaq = 1
        Chuck = int(Chuck)
        Shaq = int(Shaq)
        df_toAppend = pd.DataFrame([[videoName,time,ISO,Shaq,Chuck]],columns=colNames)
        df = df.append(df_toAppend)

df.reset_index(inplace=True,drop=True)


resultFileName = '/tmp/Azure_' + videoName + '_result.csv'

f = open("%s"%resultFileName,"w+")
f.close()
df.to_csv("%s"%resultFileName)
uploadKeyName = srcKey.rsplit("/",1)[0] + "/Azure_Results.csv"
s3.meta.client.upload_file("%s"%resultFileName,srcBucket,uploadKeyName)
