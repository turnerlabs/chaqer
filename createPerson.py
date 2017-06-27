import sys
import chaqer
from chaqer import Chaqer
chaqerObject = Chaqer()
try:
    groupID = sys.argv[1]
except:
    print 'Please pass Group ID you want to add person to as an argument'
    sys.exit()
try:
    personName = sys.argv[2]
except:
    print 'Please pass Person Name as an argument'
    sys.exit()
try:
    personInfo = sys.argv[3]
except:
    personInfo = ""
chaqerObject.createPerson(groupID,personName,personInfo)
