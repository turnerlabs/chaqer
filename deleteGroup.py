import sys
import chaqer
from chaqer import chaqer
chaqerObject = chaqer()
try:
    groupID = sys.argv[1]
except:
    print 'Please enter ID of the group you want to delete as an argument'
chaqerObject.deleteGroup(groupID)
