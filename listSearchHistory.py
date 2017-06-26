import chaqer
from chaqer import Chaqer
import sys
chaqerObject = Chaqer()
try:
    groupID = sys.argv[1]
except:
    print 'Please pass the ID of the group you want the search history as an argument '
    sys.exit()
chaqerObject.listSearchHistory(groupID)
