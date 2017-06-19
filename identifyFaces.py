import httplib, urllib, base64
import json
import os
import sys

key = str(os.environ.get('subscriptionKey'))
person1ID = str(os.environ.get('person2ID'))
person2ID = str(os.environ.get('person1ID'))

def detectFaces():

    headers = {
        # Request headers
        #For readin image from local uncomment application/octet-stream line and comment application/json line
        #'Content-Type': 'application/octet-stream',
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key,
    }

    params = urllib.urlencode({
        # Request parameters
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
    })

    ### For reading image from local uncomment the lines below and comment out the 'URL' line

    #with open("/Users/varunvohra/Desktop/shaq-big-show.jpg","rb") as img:
    #    body = img.read()
    #Enter the url of image you want to test on below
    body = "{'url':'YourURL'}"

    try:
        #Enter appropriate region for your Azure account
        conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        data = json.loads(data)
        conn.close()
        return([d['faceId'] for d in data])
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def identifyFaces():
    person1FLAG = -1
    person2FLAG = -1

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key,
    }

    faceId = detectFaces(sendURL)
    if len(faceId)!=0:
        faceId = str(faceId)
        faceId = faceId.replace("u","")

        params = urllib.urlencode({
        })

        body = "{'personGroupId':'chaq','faceIds':%s,'maxNumOfCandidatesReturned':1,'confidenceThreshold':0.6}" %faceId

        try:
            #Enter appropriate region for your Azure account
            conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/identify?%s" % params, body, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
            data = json.loads(data)
            #print data[1]["candidates"][0]["personId"]
            for i in range(0,len(data)):
                if len(data[i]["candidates"]) != 0:
                    if data[i]["candidates"][0]["personId"] == person1ID:
                        person1FLAG = person1FLAG + 1
                    elif data[i]["candidates"][0]["personId"] == person2ID:
                        person2FLAG = person2FLAG + 1
                    else:
                        continue
                else:
                    continue
            if person1FLAG != -1:
                outStr = 'Person1: Yes'
            else:
                outStr = 'Person1: No'

            if person2FLAG != -1:
                outStr = outStr + '\nPerson2: Yes'
            else:
                outStr = outStr + '\nPerson2: No'
        except Exception as e:
            print e
    else:
        outStr = 'No Faces Found'

    return outStr

if __name__ == '__main__':
    outStr = identifyFaces()
    print outStr
