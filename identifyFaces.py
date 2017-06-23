import sys
import os
import chaqer
from chaqer import chaqer
chaqerObject = chaqer()
try:
    groupID = sys.argv[1]
except:
    print 'Please enter the ID of the group you want to search on as argument'
try:
    img = sys.argv[2]
except:
    print 'Please enter image as an argument'
flag = -1

try:
    with open('%s'%img) as f:
        flag = -1
except:
    try:
        with open('%s'%img) as f:
            flag = -1
    except Exception as e:
        if 'Is a directory' in e:
            flag = 1
        else:
            continue
if flag == -1:
    chaqerObject.identifyFaces(groupID,img)
else :
    filePath = os.listdir('%s'%img)
    if any('.DS_Store' in s for s in filePath):
        filePath.remove(".DS_Store")
    for i in range(0,len(filePath)):
        fileName = str(img) + filePath[i]
        chaqerObject.identifyFaces(groupID,fileName)
