import sys
import chaqer
from chaqer import chaqer
chaqerObject = chaqer()
while True:
    ch = raw_input("\n\n\n1.To create a Person Group enter 1\n2.To create a Person enter 2\n3.To add faces to a person enter 3\n4.To train a group enter 4\n5.To identify people in an image enter 5\n6.To list already existing groups enter 6\n7.To delete a group enter 7\n8.To exit enter 'Exit'\n\n\n")
    ch = str(ch)
    if ch == '1':
        groupID = raw_input("\n\n\nEnter ID of the group you want to create (Lowercase alphabets and numbers only): ")
        groupName = raw_input("\n\n\nEnter the name of your Group: ")
        groupInfo = raw_input("\n\n\nEnter info about your group (This field is optional. Hit Enter to skip.): ")
        chaqerObject.createPersonGroup(groupID,groupName,groupInfo)
    elif ch == '2':
        groupID = raw_input("\n\n\nEnter ID of the group you want to create the person in: ")
        personName = raw_input("\n\n\nEnter the name of the Person: ")
        personInfo = raw_input("\n\n\nEnter info about the person (This field is optional. Hit Enter to skip.): ")
        chaqerObject.createPerson(groupID,personName,personInfo)
    elif ch == '3':
        personName = raw_input("\n\n\nEnter the name of the person you want to add face(s) to: ")
        groupID = raw_input("\n\n\nEnter the groupID of the person: ")
        img = raw_input("\n\n\nEnter URL or path to image or path of directory containing images: ")
        chaqerObject.addFace(groupID,personName,img)
    elif ch == '4':
        groupID = raw_input("\n\n\nEnter the ID of the group you want to train: ")
        chaqerObject.trainGroup(groupID)
    elif ch == '5':
        groupID = raw_input("\n\n\nEnter the ID of the group you want to check on: ")
        img = raw_input("\n\n\nEnter URL or local path of image you want to identify faces on: ")
        chaqerObject.identifyFaces(groupID,img)
    elif ch == '6':
        chaqerObject.listGroups()
    elif ch == '7':
        groupID = raw_input("\n\n\nEnter ID of the group you want to delete: ")
        chaqerObject.deleteGroup(groupID)
    elif ch == 'exit' or ch == 'Exit':
        print '\n\n\n\n'
        sys.exit()
