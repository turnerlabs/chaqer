import sys
import chaqer
from chaqer import chaqer
chaqerObject = chaqer()
try:
    groupID = sys.argv[1]
except:
    print 'Please pass ID of the group you want to train as an argument'
chaqerObject.trainGroup(groupID)
