import os
import sys
#lib_path = os.path.abspath(os.path.join('lib'))
#sys.path.append(lib_path)
import boto3
from PIL import Image
import botocore
import io
import urllib
import boto
import zipfile
import pandas as pd
import datetime

def recogniseCelebs(srcBucket,srcKey):
    #try:
    client = boto3.client('rekognition')
    resource = boto3.resource('s3')
    s3 = boto3.resource('s3')
    localFilename = '/tmp/{}'.format(os.path.basename(srcKey))
    try:
        s3.Bucket(srcBucket).download_file(srcKey,localFilename)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
    zip_ref = zipfile.ZipFile(localFilename, 'r')
    zip_ref.extractall('/tmp/')
    zip_ref.close()
    #Create DataFrame
    colNames = ['VideoName','ImageName','ISO','TimeStamp','Celebrities']
    df = pd.DataFrame(columns=colNames)
    #Getting video name from the path of zip file with images
    videoName = str(srcKey.rsplit("/",2)[1])
    for imgFile in sorted(os.listdir('/tmp/')):
        if imgFile.find("img") != -1:
            #img = str(f.key)
            with open('/tmp/' + imgFile, "rb") as imageFile:
                slicedImage = imageFile.read()
                imgBytes = bytearray(slicedImage)
                response = client.recognize_celebrities(
                    Image={
                        'Bytes': imgBytes,
                    }
                )

                #To add millisec to the timeformat
                mili = '000'
                ID = os.path.basename(imgFile)
                imageName = format(os.path.basename(imgFile))
                #Get the seconds information of the frame
                time = float(ID.split("_",1)[0])
                iso = str(datetime.timedelta(seconds=time))
                strTime = iso.rsplit(".",1)[0]
                try:
                    mili = iso.rsplit(".",1)[1]
                    mili = mili[:-3]
                except:
                    pass
                iso = strTime+":"+mili
                for i in range (0,len(response['CelebrityFaces'])):
                    celebName = response['CelebrityFaces'][i]['Name']
                    df_toAppend = pd.DataFrame([[videoName,imageName,iso,time,celebName]],columns=colNames)
                    df = df.append(df_toAppend)
    df.reset_index(inplace=True,drop=True)
    resultFileName = '/tmp/AWS_' + videoName + '_result.csv'
    f = open("%s"%resultFileName,"w+")
    f.close()
    df.to_csv("%s"%resultFileName)
    name = str(srcKey.rsplit("/",1)[0]+"/"+"AWS_result.csv")
    object = s3.Bucket(srcBucket).put_object(Body = open(resultFileName), Key = name)
    # except Exception as e:
    #                 print e


if __name__ == '__main__':
    srcBucket = str(os.environ.get('LOCALBUCKET'))
    srcKey = str(os.environ.get('FILE'))
    recogniseCelebs(srcBucket,srcKey)
    #recogniseCelebs(srcBucket,srcKey)
