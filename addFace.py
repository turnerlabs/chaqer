import sys
import chaqer
from chaqer import chaqer
chaqerObject = chaqer()
try:
    groupID = sys.argv[1]
except:
    print 'Please pass Group ID of the person as argument'
try:
    personName = sys.argv[2]
except:
    print 'Please pass the name of the person you want add face(s) to as argument'
try:
    img = sys.argv[3]
except:
    print 'Please pass image as argument'

groupID = chaqerObject.addFace(groupID,personName,img)
