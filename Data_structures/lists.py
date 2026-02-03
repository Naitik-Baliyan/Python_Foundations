#List in python 

#Creating a list 
numbers = [10, 20, 30, 40]

#accessing elements
print(numbers[0])
print(numbers[-1])

#Adding elements 
numbers.append(60)
print(numbers)

#Removing elements 
numbers.remove(20)
print(numbers)

#Looping through a list 
for num in numbers:
    print(num) 
