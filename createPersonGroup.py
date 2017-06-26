import sys
import chaqer
from chaqer import Chaqer
chaqerObject = Chaqer()
try:
    groupID = sys.argv[1]
except:
    print 'Please pass Group ID as an argument'
    sys.exit()
try:
    groupName = sys.argv[2]
except:
    print 'Please pass group Name as an argument'
    sys.exit()
try:
    groupInfo = sys.argv[3]
except:
    groupInfo = ""
chaqerObject.createPersonGroup(groupID,groupName,groupInfo)
