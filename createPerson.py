import sys
import chaqer
from chaqer import chaqer
chaqerObject = chaqer()
try:
    groupID = sys.argv[1]
except:
    print 'Please pass Group ID you want to add person to as an argument'
try:
    personName = sys.argv[2]
except:
    print 'Please pass Person Name as an argument'
try:
    personInfo = sys.argv[3]
except:
    personInfo = ""
chaqerObject.createPerson(groupID,personName,personInfo)
