# Enumerate adds index to elements when looping
#Example 1
fruits ={'apple', 'banana', 'cherry'} #Sets are unordered collections
for index, item in enumerate(fruits):
    print(f"{index}: {item}")

#Example 2
print("--------------------------------------")
word = "hello"
for i, char in enumerate(word):
    print(f"Position {i+1}: {char}")

#Example 3
print("--------------------------------------")
colors = ('red', 'green', 'blue')
for color_name in enumerate(colors):
    print(f"{color_name}")


#Example 4: list comprehension with enumerate
print("----------------------------------------------------")
square = [3,4,5]
result = [(f"{j}-{k**2}") for j,k in enumerate(square)]
print(result)
print("square with while loop")
i=0
while (i<len(square)):
    ans=square[i]**2
    print(f"square of {square[i]} is {ans}")
    i+=1



print("----------------Example:5--------------------------")
item=["banana","oats","pizza"]
number=int(input("Which number do you want to start printing the list from?--"))

for index,i in enumerate(item):
    print(f"{index+number} : {i}")

print("--------------------Example:6--------------------")
fruits=["banana","apple","pear"]
for index,i in enumerate(fruits,start=number):
     print(f"{index}:{i}")





