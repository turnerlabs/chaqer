import sys
import chaqer
from chaqer import Chaqer
chaqerObject = Chaqer()
try:
    groupID = sys.argv[1]
except:
    print 'Please enter ID of the group you want to delete as an argument'
    sys.exit()
chaqerObject.deleteGroup(groupID)
