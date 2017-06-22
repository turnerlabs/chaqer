# Chaqer
Program to check if a person is in the image or not

Before running the programs in the order mentioned below export your Ocp-Apim-Subscription-Key you got from Microsoft as an environment variable

```
export SUBSCRIPTION_KEY=Your-Ocp-Apim-Subscription-Key
export AZURE_REGION=Your_Region
```

### Create Person Group
Run the createPersonGroup program to create a new group for the people you want the chaqer to check on
Pass :-
- Group ID as the first argument (Lower case alphabets and Numbers only)
- Group Name as the second argument (Optional)
- Group Info as the third argument (Optional)

```python createPersonGroup.py your_group_id your_group_name your_group_info```

### Create Person
Run the createPerson program to create a person in the group you created above
Pass :-
- ID of the group you want to create the person in as first argument
- Person name as the second argument
- Person Info as the third argument

``` python createPerson.py group_id person_name person_info ```

### Add Faces to a person
Run the program addFace to add faces to a person
Pass :-
- ID of the group the person belongs to as the first argument
- Name of the person you want to add faces to as the second argument
- URL of image of the person or local path of an image or path of a directory containing images of the person as the third argument

``` python addFace.py group_id person_name the_image```


### Train your group
Run the program trainGroup to train a group on the faces you have provided
Pass :-
- The ID of the group you want train

``` python trainGroup.py group_id```

### Identify faces
Run the program identifyFaces to identify faces in an image you provide
Pass :-
- The ID of the group you want to check on as the first argument
- URL of image of the person or local path of an image as

``` python identifyFaces.py group_id the_image```

### List Person Groups
Run the program listGroups to list already existing Groups

```python listGroups.py ```

### Delete Person Group
Run the program deleteGroup to delete a group
Pass :-
- The ID of the group you want to delete as an argument

``` python deleteGroup.py group_id ```

### Run the chaqer app
Run the chaqer app for interactive chaqing

``` python runchaqer.py ```
