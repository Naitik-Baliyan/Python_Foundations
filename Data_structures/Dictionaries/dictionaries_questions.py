#Priblem 1 : Count frequency of characters in a string 
s = "Engineering"
freq = {}
for ch in s :
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

#Problem 2 : Find the key with maximum value 
marks = { 
    "Anil" : 45,
    "Sunil" : 50, 
    "Naitik" : 50, 
    "Ajay" : 45
}
topper = max(marks, key = marks.get)
print(topper, marks[topper])

#Problem 3 : Nested dictionary- Student details 
students = {
    1: {"Name": "Aman", "Marks": 74}, 
    2: {"Name": "Naitik", "Marks": 78}
}
for roll, info in students.items:
    print(roll, info["Name"], info["Marks"])