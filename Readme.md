# Chaqer
Program to check if a person is in the image or not

Before running the programs in the order mentioned below export your Ocp-Apim-Subscription-Key you got from Microsoft as an environment variable

```export SUBSCRIPTION_KEY=Your_Ocp-Apim-Subscription-Key
export AZURE_REGION=Your_Region```

### Create Person Group
Run the createPersonGroup program to create a new group for the people you want the chaqer to check on
Pass :-
- Group ID as the first argument (Lower case alphabets and Numbers only)
- Group Name as the second argument (Optional)
- Group Info as the third argument (Optional)

```python createPersonGroup.py your_group_id your_group_name your_group_inf0```

### Create Person
Run the createPerson program to create a person in the group you created above
Pass :-
-

### Add Faces to a person
Run the program addFace to add faces to the person you created above
Input the following fields in the script before executing :-
- GroupId of the person you want to add the face to
- PersonId of the person you created above and exported as an environment variable
- Path to your folder containing the images of the person (NOTE: This folder should only contain images of the person)
- Or Path to the image you want to add
- Enter the appropriate region for your Azure account

### Train your group
Once you have added faces to the persons in your group, run the trainGroup program to train the model for the faces provided
Input the following fields in the script before executing :-
- GroupId of the group you want to trainGroup
- Enter the appropriate region for your Azure account

### Identify faces
Once you have run all the above programs, the model is ready to identify people in an image you provide
This program has two functions identifyFaces() and detectFaces(). The program uses the function detectFaces() to return an array of faceIds found in the image provided to the identifyFaces function. The identifyFaces() function returns if the person is present in the image or not.
Input the following fields in the script before executing :-
- The path or the URL of the image to check for persons
- The confidence with which you want your match to be returned
- Enter the appropriate region for your Azure account
