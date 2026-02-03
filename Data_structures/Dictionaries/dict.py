#Creating a dictionary 
student = {
    "name": "Naitik",
    "age": 18,
    "branch": "CSE"
}

#Accessing value 
print(student["name"]) 
#or
print(student.get("age"))

#add/update
student["age"] = 19
student["college"] = "ABC"

#Delete
del student["branch"]

#Loop through dictionary 
for key, value in student.items():
    print(key, ":", value)