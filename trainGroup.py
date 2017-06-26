import sys
import chaqer
from chaqer import Chaqer
chaqerObject = Chaqer()
try:
    groupID = sys.argv[1]
except:
    print 'Please pass ID of the group you want to train as an argument'
    sys.exit()
chaqerObject.trainGroup(groupID)
