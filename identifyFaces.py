import sys
import chaqer
from chaqer import chaqer
chaqerObject = chaqer()
groupID = sys.argv[1]
img = sys.argv[2]
chaqerObject.identifyFaces(groupID,img)
