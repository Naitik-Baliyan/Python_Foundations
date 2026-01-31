#Problem 1: Variable Assign & Printt
Name = "Naitik"
Age  = 19
Height = 5.11
print(Name, Age, Height) 
#Problem 2: Data Types
x = 10          # Integer
y = 3.14        # Float
z = "Hello"     # String    
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>   
print(type(z))  # Output: <class 'str'>
#Problem 3: User Input
Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
print("Hello", Name, "You are", Age, "years old.", "Next year you will be", Age + 1, "years old.")
#Problem 4: Multiple Assignments
a, b, c = 5, 10.5, "Python" 
print(a, b, c)
#Problem 5: Type Casting
num_str = "100"
num_int = int(num_str)  
num_float = float(num_str)
print(type(num_int), type(num_float))     