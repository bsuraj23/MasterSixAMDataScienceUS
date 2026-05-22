# Lambda is a small anonymous function
#Example1:
name_of_function = lambda x: f"something with {x}"
print(name_of_function(6))

#Example2
print("--------------------------------------------")
from functools import reduce
numbers=[2,3,4,5,6]
ans=reduce(lambda x,y : x+y, numbers) 
print(ans)

#Example3: sum of two list with zip function
print("---------------------------------------------------")
a = [1, 2, 3]
b = [4, 5, 6]
result = []
for x, y in zip(a, b):
    result.append(x + y)
print(result)


