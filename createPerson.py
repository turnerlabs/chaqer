import httplib, urllib, base64
import json
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '1553352b15f14991a1dda4a8742b10dd',
}


#Enter the group Id of the group you created
params = urllib.urlencode({
    'personGroupId' : 'chaq'
})

#Enter the name of the person you want to add to the group
body = "{'name':'Charles Barkley}"
body = json.dumps(body)

try:
    #Enter the appropriate region for you Azure account
    conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
