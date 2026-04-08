
# Regular function that doubles a number — has a name, saved for reuse
def double(x):
    return x * 2
#calling the function and printing the result
print(f'result:',double(4))

# Lambda — same thing, one line, no name
lambda x: x * 2  #just defining the function, doesn't do anything
print((lambda x: x * 2)(5)) #defining and passing the input and printing in one line
print((lambda x, y: x * y)(3, 4)) #multi variable input

#regular user defined funtion that returns the square of a number
def square(x):
    return x ** 2

print(f'Square:',square(5))  # → 25

# squaring a number using lamda
print(f'square using lamda:', (lambda x: x ** 2)(8))



# greeting function
def greet(name):
    return f"Hi, {name}!"

print(greet("sriram"))
# → "Hi, sriram!"

#using lambda — greeting, naming a lamda is not a good practice
greet = lambda name: f"Hi, {name}!"
print(greet("Sara"))
# → "Hi, Sara!"

print((lambda name: f"Hi, {name}!")("Sara"))



#conditional expressions
# absolute value of a number
absolute = lambda x: x if x >= 0 else -x
absolute(-5)  # → 5
absolute(3)   # → 3

#another example of conditional expression
grade = lambda score: "Pass" if score >= 50 else "Fail"
grade(72)  # → "Pass"
grade(30)  # → "Fail"

#mapping: Apply a function to every element in a list. Returns a new list.
#Converting a list of numbers to their squares
nums = [1, 2, 3, 4]

squares = list(map(lambda x: x**2, nums))
print(squares)

# another example of mapping with conditional expression
myList = [1,-1,2,-3,5]
result = list(map(lambda x: x if x >= 0 else -x, myList))
print(result)

#Filtering out negative numbers using lamda
nums = [1, 2, -3, -4, 5, -6]

positives = list(filter(lambda x: x > 0, nums))
print(positives)

#Sorting by salary
employees = [
    {"name": "Aman", "salary": 59000},
    {"name": "Beth", "salary": 70000},
    {"name": "Charlie", "salary": 68000}
]
#sorting salary in ascending order 
sorted_emp = sorted(employees, key=lambda x: x["salary"])
print(sorted_emp)
#sorting salary in descending order
sorted_emp = sorted(employees, key=lambda x: x["salary"],reverse=True)
print(sorted_emp)


#sorting the data, very useful
#Sorting a list of tuples by second value

data = [(1, 3), (2, 1), (4, 2)]

sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

# pandas with lamda: In data analysis, lambdas are used daily with apply() to transform columns.
import pandas as pd

df = pd.DataFrame({
    "name": ["ali", "sara", "mia"],
    "salary": [50000, 75000, 90000],
    "score": [45, 82, 60]
})

# Capitalise names
df["name"] = df["name"].apply(lambda x: x.title())
print(df["name"])

# Add tax column (20%)
df["tax"] = df["salary"].apply(lambda x: x * 0.20)
print(df["tax"])

# Add pass/fail based on score
df["result"] = df["score"].apply(
    lambda x: "Pass" if x >= 50 else "Fail")
print(df["result"])


