import httplib, urllib, base64
import os
import sys

key = str(os.environ.get('subscriptionKey'))

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': key,
}

#Enter the groupId of the group you want to train
params = urllib.urlencode({
    'personGroupId' : 'chaq'
})

body = ""

try:
    #Enter appropriate region for your Azure account
    conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/train?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
