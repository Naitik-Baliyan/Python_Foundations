#Loops are used to repeat instructions 
#Syntax - While condtion: 
            #some work 
#Example
count = 1 
while count <= 2:
    print("Hello")
    count += 1
#Break & Continue : 
#Break : Used to terminate the loop when encountered
print("Heyy")
i = 1
while i <=5:
    print(i)
    if(i == 3):
        break
    i +=1 
print("Loop Ended")
#Continue : Terminates execution in the current iteration & continue execution of the loop with the next iteration 
i = 1
while i <=5:
    print(i)
    if(i == 3):
        i+=1
        continue
    print(i)
    i +=1
#For Loops : sequential traversal
nums= [45, 50, 78, 554]
for val in nums:
    print(val)
#Range(): Returns a sequence of numbers, starting from 0 by default, and increaments by 1 and stops before a specified number
#range(start?, stop, step?)
for i in range(2, 100, 2):
    print (i)