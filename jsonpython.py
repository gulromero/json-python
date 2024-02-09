import json


#PYTHON JSON EXERCISES - PART 1:

#Creating a dictionary
myobject = {"ID": 1, "Name": "Gülsüm", "Age": 25, "Description": "My fav color is pink"}

#Printing the dictionary
print(myobject["ID"], myobject["Name"], myobject["Age"], myobject["Description"])


# PART 2: SERIALIZATION::

# Serializing the dictionary with the json.dumps method: 
json.dumps(myobject)

#Assigning the returned string from the past method to a variable:
manualSerialized = json.dumps(myobject)

#printing the serialized dictionary to console:
print(manualSerialized)


#PART 3: DESERIALIZATION
