#Problem 1 : Print numbers from 1 to 10 
for i in range (1, 11):
    print (i)

#Problem 2 :  sum of first n numbers 
n = int(input("Enter n : "))
total = 0 
for i in range (1, n+1):
    total += i
    print("Sum: ", total) 

#problem 3 : Countdown using while Loop 
count = 5 
while count > 0:
    print(count)
    count -= 1        