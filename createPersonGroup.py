import httplib, urllib, base64
key = str(os.environ.get('subscriptionKey'))


headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': key,
}

# Enter you unique Group ID (Lower Case and Numbers only)
params = urllib.urlencode({
    'personGroupId' : 'chaq'
})

#Enter the name of your group and user data (Name is required and user data is optional)

body = "{'name':'Chuck and Shaq','userData':''}"

try:
    #Enter your appropriate region for your Azure account
    conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
    conn.request("PUT", "/face/v1.0/persongroups/{personGroupId}?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
