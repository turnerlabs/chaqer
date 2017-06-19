import httplib, urllib, base64
import json
import os
import sys

key = str(os.environ.get('subscriptionKey'))

headers = {
    # Request headers
    #To read image from a URL uncomment application/json
    #'Content-Type': 'application/json'
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': key,
}

params = urllib.urlencode({
    # Request parameters
    # Enter the groupId of the person you want to add the face to.
    'personGroupId': 'chaq',
    # Get the personID of the person you want to add the face to.
    'personId': str(os.environ.get('CHUCKID'))
})


#Enter path to your folder here
personFilePath = os.listdir("/Users/varunvohra/Documents/Chuck")
#NOTE: All files in the directory must be images of the person whose face you want to add.

#For Mac Users
if any('.DS_Store' in s for s in personFilePath):
    personFilePath.remove(".DS_Store")

## Add all files in a directory

for i in range (0,len(chuckFilePath)):
    filePath = "/Users/varunvohra/Documents/Chuck/" + str(personFilePath[i])
    with open (filePath,"rb") as img:
        body = img.read()
    try:
        #Enter appropriate region for your Azure account
        conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons/{personId}/persistedFaces?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

## Add one file

#Enter path of the image
with open ("/Users/varunvohra/Desktop/la-sp-kobe-shaq-20160417","rb") as img:
    body = img.read()
try:
    #Enter appropriate region for your Azure account
    conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons/{personId}/persistedFaces?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
