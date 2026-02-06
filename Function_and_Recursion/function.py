#Functions : Block of statements that perform a specific task 
#Example 1 : 
def calc_sum(a, b):
    sum = a + b 
    print (sum)
    return sum 
calc_sum(5, 10) 
#Example 2 :
def print_hello():
    print("Hello")
    return print_hello
print_hello() 
#Average of three numbers 
def avrg(a, b, c):
    average = (a+b+c)/3 
    print(average)
    return average 
avrg(1, 2, 3)
#Types of functions - Built-in functions(len, print, type, range), user-defined functions
#Problem 1 : WAF to print the length of the list 
cities = ["Delhi", "Gurugram", "Mumbai", "Kanpur", "Mathura"]
Actors = ["Akshay kumar", "Salman Khan", "Akshay Khanna", "Ranveer Singh", "Ranbeer Kapoor"]
def print_Len(list):
    print(len(list))
print_Len(cities)
print_Len(Actors)