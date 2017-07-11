import httplib, urllib, base64
import os
import sys
import json
import time

class Chaqer:

    def __init__(self):
        self.KEY =str(os.environ.get('SUBSCRIPTION_KEY', ""))
        self.REGION = str(os.environ.get('AZURE_REGION', ""))
        self.CONN_CODE = self.REGION + '.api.cognitive.microsoft.com'
        self.NameID = {}

        self.headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.KEY,
        }

        if self.KEY == "" or self.REGION == "":
            print "Must have SUBSCRIPTION_KEY and AZURE_REGION set"
            sys.exit()

    def deleteGroup(self,groupID):
        params = urllib.urlencode({
            'personGroupId' : groupID
        })
        try:
            conn = httplib.HTTPSConnection(self.CONN_CODE)
            conn.request("DELETE", "/face/v1.0/persongroups/{personGroupId}?%s" % params, "{body}", self.headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            fileName = '/tmp/' + groupID.lower() + '.txt'
            os.remove('%s'%fileName)
            responseFileName = '/tmp/' + 'imagesSearchedOn' + groupID.upper() + '.txt'
            os.remove('%s'%responseFileName)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))





    def listGroups(self):
        params = urllib.urlencode({
        })

        try:
            conn = httplib.HTTPSConnection(self.CONN_CODE)
            conn.request("GET", "/face/v1.0/persongroups?%s" % params, "{body}", self.headers)
            response = conn.getresponse()
            data = response.read()
            data = json.loads(data)
            for i in range(0,len(data)):
                print '\n\nGroupID: ' + str(data[i]["personGroupId"])
                print 'Group Name: ' + str(data[i]["name"])
                print 'Group Info: ' + str(data[i]["userData"])
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))




    def createPersonGroup(self,groupID,groupName="",groupInfo=""):
        emptyDict = {}
        groupID = str(groupID)
        params = urllib.urlencode({
            'personGroupId' : groupID
        })

        body = "{'name': '%s' ,'userData':'%s'}" %(groupName,groupInfo)
        try:
            conn = httplib.HTTPSConnection(self.CONN_CODE)
            conn.request("PUT", "/face/v1.0/persongroups/{personGroupId}?%s" % params, body, self.headers)
            response = conn.getresponse()
            data = response.read()
            if data != '':
                print '\n\n\n' + data
                return
            print '\n\n\nSuccesfully Created Group \n' + 'Group ID: ' + groupID + '\nGroup Name: ' + groupName + '\nGroup Info: ' + groupInfo
            print data
            conn.close()
            responseFileName = '/tmp/' + 'imagesSearchedOn' + groupID.upper() + '.txt'
            e = open('%s'%responseFileName,'w+')
            e.close()
            fileName = '/tmp/' + groupID.lower() + '.txt'
            f = open('%s'%fileName,'w+')
            f.close()
        except Exception as e:
            print e
            print("[Errno {0}] {1}".format(e.errno, e.strerror))





    def createPerson(self,groupID,personName,personInfo=""):
        groupID = str(groupID)
        params = urllib.urlencode({
            'personGroupId' : groupID
        })
        NAME = personName.upper()
        body = "{'name': '%s' ,'userData':'%s'}" %(personName,personInfo)

        try:
            conn = httplib.HTTPSConnection(self.CONN_CODE)
            conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons?%s" % params, body, self.headers)
            response = conn.getresponse()
            data = response.read()
            if 'NotFound' in data:
                print '\n\n\nNo Group with ID ' + groupID + ' exists'
                return
            print '\n\n\nSuccessfully created ' + str(personName)
            print data
            data = json.loads(data)
            ID = data['personId']
            ID = str(ID)
            fileName = '/tmp/' + groupID.lower() + '.txt'

            if os.stat('%s'%fileName).st_size != 0:
                with open('%s'%fileName,'r') as f:
                    self.NameID = eval(f.read())

            self.NameID[NAME] = ID

            with open('%s'%fileName,'w') as f:
                json.dump(self.NameID,f)

            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))




    def addFace(self,groupID,personName,image):
        groupID = str(groupID)
        flag = -1
        count = 0
        name = personName.lower()
        NAME = personName.upper()
        fileName = '/tmp/' + groupID.lower() + '.txt'
        try:
            if os.stat('%s'%fileName).st_size == 0:
                print '\n\n\nPerson not avaialble. Create Person first to add faces'
                return
        except:
            print '\n\nNo group by the name ' + groupID +' exists'
        try:
            with open('%s'%fileName,'r') as f:
                self.NameID = eval(f.read())
        except:
            print '\n\n\nNo group with ID ' + groupID + ' exists'
            return


        personID = self.NameID[NAME]

        params = urllib.urlencode({
            'personGroupId': groupID,
            'personId': personID
        })
        body = "{'url':'%s'}" %image
        try:
            conn = httplib.HTTPSConnection(self.CONN_CODE)
            conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons/{personId}/persistedFaces?%s" % params, body, self.headers)
            response = conn.getresponse()
            data = response.read()
            if 'NotFound' in data:
                print data
                return
            data = json.loads(data)
            if 'error' not in data.keys():
                print 'Succesfully added face to ' + personName
                flag = 1
            ##Enter here if not URL
            elif flag == -1:
                localHeaders = {
                    'Content-Type': 'application/octet-stream',
                    'Ocp-Apim-Subscription-Key': self.KEY,
                }
                try:
                    with open('%s'%image,'rb') as img:
                        body = img.read()

                    conn = httplib.HTTPSConnection(self.CONN_CODE)
                    conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons/{personId}/persistedFaces?%s" % params, body, localHeaders)
                    response = conn.getresponse()
                    data = response.read()
                    if 'NotFound' in data:
                        print '\n\n\n' + data
                        return
                    data = json.loads(data)
                    if 'error' not in data.keys():
                        print '\n\n\nSuccesfully added face to ' + personName
                        flag = 1
                except:
                    personFilePath = os.listdir('%s'%image)

                    if any('.DS_Store' in s for s in personFilePath):
                        personFilePath.remove(".DS_Store")

                    for i in range (0,len(personFilePath)):
                        filePath = str(image) + str(personFilePath[i])
                        with open ('%s'%filePath,"rb") as img:
                            body = img.read()
                        conn = httplib.HTTPSConnection(self.CONN_CODE)
                        conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons/{personId}/persistedFaces?%s" % params, body, localHeaders)
                        response = conn.getresponse()
                        data = response.read()
                        if 'NotFound' in data:
                            print '\n\n\n' + data
                            return
                        data = json.loads(data)

                        if 'error' in data.keys():
                            print '\n\n\nCould not find face in ' + filePath
                        else:
                            count = count + 1

                    flag = 1
                    print '\n\n\nSuccessfully added ' + str(count) + ' faces to ' + str(personName)
            elif flag == -1:
                print '\n\n\nPlease provide valid image URL, local path, or directory path'
            conn.close()
        except Exception as e:
            print '\n\n\nEnter valid URL, local path or directory path'
            #print("[Errno {0}] {1}".format(e.errno, e.strerror))





    def trainGroup(self,groupID):
        params = urllib.urlencode({
            'personGroupId' : groupID
        })
        body=''
        try:
            conn = httplib.HTTPSConnection(self.CONN_CODE)
            conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/train?%s" % params, body, self.headers)
            response = conn.getresponse()
            data = response.read()
            if 'NotFound' in data:
                print '\n\n\nGroup with groupID ' + groupID + ' does not exist'
                return
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))





    def detectFaces(self,img):
        params = urllib.urlencode({
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
        })
        body = "{'url':'%s'}" %img
        try:
            conn = httplib.HTTPSConnection(self.CONN_CODE)
            conn.request("POST", "/face/v1.0/detect?%s" % params, body, self.headers)
            response = conn.getresponse()
            data = response.read()

            if 'error' not in data:
                data = json.loads(data)
                return ([d['faceId'] for d in data])

            elif True:
                with open(img,'rb') as img:
                    body = img.read()
                localHeaders = {
                    'Content-Type': 'application/octet-stream',
                    'Ocp-Apim-Subscription-Key': self.KEY,
                }
                conn = httplib.HTTPSConnection(self.CONN_CODE)
                conn.request("POST", "/face/v1.0/detect?%s" % params, body, localHeaders)
                response = conn.getresponse()
                data = response.read()
                if 'error' not in data:
                    data = json.loads(data)

                    return ([d['faceId'] for d in data])

            return 'exit'
            conn.close()
        except Exception as e:
            return 'exit'





    def identifyFaces(self,groupID,image):
        outStr = ' '
        jsonName = []
        result = {}
        imgResult = {}
        responseFileName = '/tmp/' + 'imagesSearchedOn' + groupID.upper() + '.txt'
        params = urllib.urlencode({
        })
        faceID = Chaqer().detectFaces(image)
        if faceID == 'exit':
            print '\n\n\n Unexpected input format'
            return
        elif len(faceID) == 0:
            print '\n\n\nNo Faces found in ' + image
            if os.stat('%s'%responseFileName).st_size != 0:
                with open('%s'%responseFileName,'r') as f:
                    result = eval(f.read())
            result[image] = jsonName
            with open('%s'%responseFileName,'w') as f:
                json.dump(result,f)
            return
        else:
            faceID = str(faceID)
            body = "{'personGroupId':'%s','faceIds':%s,'maxNumOfCandidatesReturned':1,'confidenceThreshold':0.6}" %(groupID,faceID)
            try:
                conn = httplib.HTTPSConnection(self.CONN_CODE)
                conn.request("POST", "/face/v1.0/identify?%s" % params, body, self.headers)
                response = conn.getresponse()
                data = response.read()
                if 'BadArgument' in data:
                    print '\n\n\n' + data
                    return
                conn.close()
                data = json.loads(data)
            except Exception as e:
                print("[Errno {0}] {1}".format(e.errno, e.strerror))

            fileName = '/tmp/' + groupID.lower() + '.txt'
            with open('%s'%fileName,'r') as f:
                self.NameID = eval(f.read())
            for i in range(0,len(data)):
                if len(data[i]["candidates"]) != 0:
                    if data[i]["candidates"][0]["personId"] in self.NameID.values():
                        tempDict = {}
                        name = self.NameID.keys()[self.NameID.values().index(data[i]["candidates"][0]["personId"])]
                        outStr = outStr + name + ', '
                        tempDict['Name'] = name
                        tempDict['Confidence'] = data[i]["candidates"][0]["confidence"]
                        jsonName.append(tempDict)
                    else:
                        pass
                else:
                    pass
            outStr = outStr[:-2]
            if outStr == '':
                print '\n\n\nCouldn\'t identify anyone'
                if os.stat('%s'%responseFileName).st_size != 0:
                    with open('%s'%responseFileName,'r') as f:
                        result = eval(f.read())
                result[image] = jsonName
                with open('%s'%responseFileName,'w') as f:
                    json.dump(result,f)
                return

            print '\n\n\nSuccesfully identified ' + outStr + ' in the image ' + str(image)
            if os.stat('%s'%responseFileName).st_size != 0:
                with open('%s'%responseFileName,'r') as f:
                    result = eval(f.read())

            result[image] = jsonName

            with open('%s'%responseFileName,'w') as f:
                json.dump(result,f)
        print '\n\n\n'
        print jsonName
        print '\n\n\n'
        return

    def identifyFacesS3(self,groupID,image):
        result = {}
        finalResult = []
        params = urllib.urlencode({})
        faceID = Chaqer().detectFaces(image)
        if len(faceID) == 0:
            return 0
        else:
            faceID = str(faceID)
            body = "{'personGroupId':'%s','faceIds':%s,'maxNumOfCandidatesReturned':1,'confidenceThreshold':0.6}" %(groupID,faceID)

            try:
                conn = httplib.HTTPSConnection(self.CONN_CODE)
                conn.request("POST", "/face/v1.0/identify?%s" % params, body, self.headers)
                response = conn.getresponse()
                data = response.read()
                conn.close()
                data = json.loads(data)

                if not isinstance(data, (list, tuple)) == True:
                    if data["error"]:
                        print data["error"]["message"]
                        print data["error"]["code"]

                        if data["error"]["code"] == "RateLimitExceeded":
                            time.sleep(5)
                            self.identifyFacesS3(groupID,image)
                        else:
                            raise Exception('unkown error! ' + data["error"]["code"] + " : " + data["error"]["message"] + " for " + image)

                for i in range(0,len(data)):
                    if len(data[i]["candidates"]) != 0:
                        name = Chaqer().getPerson("chaqer",data[i]["candidates"][0]["personId"])
                        confidence = data[i]["candidates"][0]["confidence"]
                        result["Name"] = name
                        result["Confidence"] = confidence
                        finalResult.append(result)

            except Exception as e:
                print e

            return finalResult

    def getPerson(self,groupID,personID):
        params = urllib.urlencode({
            'personGroupId': groupID,
            'personId': personID,
        })

        try:
            conn = httplib.HTTPSConnection(self.CONN_CODE)
            conn.request("GET", "/face/v1.0/persongroups/{personGroupId}/persons/{personId}?%s" % params, "{body}", self.headers)
            response = conn.getresponse()
            data = response.read()
            data = json.loads(data)
            conn.close()
            return data["name"]
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

    def listSearchHistory(self,groupID):
        responseFileName = '/tmp/' + 'imagesSearchedOn' + groupID.upper() + '.txt'
        with open('%s'%responseFileName,'r') as f:
            result = eval(f.read())
        print result
        print '\n\n\n'
