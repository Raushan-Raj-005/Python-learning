student ={
    "name": "Raj",
    "city": "Nalanda",
    "age": 22
}
print(student)

#  Also creating Disctionary using dict() function
student1 = dict(name="Raushan", age=25, city="Bihar")


#Accessing 

print(student1)
print(student1["name"])
print(student1["age"])
print(student1["city"])
# print(student1["nameee"])  # Error
print(student1.get("nameee"))
print(student1.get("name"))

#updating

student1["city"]="Patna"
print(student1)


#Adding and Updating Values

student1["email"] = "test@gmail.com"
student1["contact"] = 7563007519
print(student1)

# Removing Dictionary Items
# pop()
# Removes a key and returns its value.
age = student.pop("age")
print(student)

# popitem()
# Removes and returns the last inserted key value pair
student1.popitem()
print(student1)

# del
# Deletes a key value pair.
del student1["city"]
print(student1)

# clear()
# Removes all items from the dictionary
student.clear()
print(student)


# Dictionary Keys, Values, and Items
print(student1.keys())
print(student1.values())
print(student1.items())

