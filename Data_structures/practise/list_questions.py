#Problem 1 : Sum of all elements in a list 
numbers = [10, 20, 30, 40]
total = 0 
for num in numbers:
    total += num
print(total)

#Problem 2 : Count even and odd
numbers = []
user_input = input("Enter numbers separated by space: ")
numbers = user_input.split() #Splits every string into a new list 
numbers = [int(num) for num in numbers]
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1 
    else :
        odd += 1
print("Numbers entered by the user: ", numbers)
print("Even Count: ", even)
print("Odd Counts: ", odd)

#Search for an elemennt 
elements = []
user_input = input("Enter the elements which you wanted to store by space: ")
elements = user_input.strip().split()
search = input("Enter the element which you wanted to search: ").strip() #strip removes extra spaces from start and end of a string
found = False
for i in elements: 
    if i == search:
        found = True
        break
if found:
    print("Element found")
else:
    print("Element not found")