import sys
import chaqer
from chaqer import chaqer
chaqerObject = chaqer()
groupID = sys.argv[1]
try:
    groupName = sys.argv[2]
except:
    groupName = ""
try:
    groupInfo = sys.argv[3]
except:
    groupInfo = ""
chaqerObject.createPersonGroup(groupID,groupName,groupInfo)
