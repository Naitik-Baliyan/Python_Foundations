#Problem 1 : Convert tuple to list 
colors = ("red", "green", "blue")
color_list = []
for colors in colors:
    color_list.append(colors)
print(color_list)

#Problem 2 : Count element frequency 
nums = (1,2, 3, 4, 5, 6, 7, 4, 7, 9, 2)
count = 0 
element = 2
for num in nums:
    if num == nums:
        count += 1
print("Frequency: ", count)

#Problem 3 : Print last element
numbers = (10, 20, 30, 40, 50)
print("Last Element: ", numbers[-1])