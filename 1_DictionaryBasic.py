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


# Coppy Variable
new_student = student.copy()
print(new_student)