import sys
import chaqer
from chaqer import chaqer
chaqerObject = chaqer()
groupID = sys.argv[1]
personName = sys.argv[2]
img = sys.argv[3]
groupID = chaqerObject.addFace(groupID,personName,img)
