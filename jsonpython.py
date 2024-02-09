import json


#PYTHON JSON EXERCISES - PART 1:

#Creating a dictionary
myobject = {"ID": 1, "Name": "Gulsum", "Age": 25, "Description": "My fav color is pink"}

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

#Deserializing and storing the result into anoter variable. 
manualDeserialized = json.loads(manualSerialized)

#printing the deserilized object
print(manualDeserialized)

#PART 4: SPECIAL CHARACTERS

manualSerialized = {"ID": 1, "Name": "Gulsu\"m", "Age": 25, "Description": "My fav color is pink"}
print(manualSerialized)

#PART 5: Working with others Json

#We're provided a JSON string that we want to deserialize into a dictionary.

json_string = {"Name":"Move Cars","Address":"MagleGaardsvej 2","Cars":[{"Brand":"BMW","Model":"330e","Color":"Green","Mileage":45721},{"Brand":"VW","Model":"Golf","Color":"Red","Mileage":20},{"Brand":"Ford","Model":"Galaxy","Color":"Black","Mileage":124326}],"Employees":[{"Name":"Move","Salary":1000000,"MonthsEmployed":28,"JobAreas":["President","Mechanic"]},{"Name":"Not Move","Salary":100,"MonthsEmployed":13,"JobAreas":["Vice-President","Mechanic"]}]}

data = json.loads(json_string)

