import chaqer
from chaqer import chaqer
import sys
chaqerObject = chaqer()
try:
    groupID = sys.argv[1]
except:
    print 'Please pass the ID of the group you want the search history as an argument '
chaqerObject.listSearchHistory(groupID)
