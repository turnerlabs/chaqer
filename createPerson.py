import sys
import chaqer
from chaqer import chaqer
chaqerObject = chaqer()
groupID = sys.argv[1]
personName = sys.argv[2]
personInfo = sys.argv[3]
chaqerObject.createPerson(groupID,personName,personInfo)
