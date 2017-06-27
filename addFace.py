import sys
import chaqer
from chaqer import Chaqer
chaqerObject = Chaqer()
try:
    groupID = sys.argv[1]
except:
    print 'Please pass Group ID of the person as argument'
    sys.exit()
try:
    personName = sys.argv[2]
except:
    print 'Please pass the name of the person you want add face(s) to as argument'
    sys.exit()
try:
    img = sys.argv[3]
except:
    print 'Please pass image as argument'
    sys.exit()
groupID = chaqerObject.addFace(groupID,personName,img)
