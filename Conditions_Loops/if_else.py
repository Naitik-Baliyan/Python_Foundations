#Problem 1 : Check whether a number is odd or even 
num = int(input("Enter the number which you wanted to check: ")) #Takes input from User
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#Problem 2 : Categrozing the age
age = int(input("Enter the age: ")) #Takes input from the user
if age < 18:
    print("Minor")
elif age < 60: 
    print("Adult") 
else:
    print("Senior Citizen")

#Problem 3 : Find the Largest number 
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a >= b and a >=c :
    print(a, "is largest")
elif b >= a and b >= c:
    print(b, "is largest")
else:
    print(c, "is largest")       