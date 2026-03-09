''' Anonumous functions: 
1. Don't have a defined name.
2. Also known as lambda functions in Python.
3. Used for short, simple functions such as sorting, filtering, or mapping data.
4. Lambda functions are also called as inline functions because they are defined in a single line of code.
4. Lambda functions are not reusable as compared with the regular functions.
5. They are defined using the lambda keyword, followed by the parameters, a colon, and the expression that defines the function's behavior.
Syntax: lambda arguments: expression'''

# Example 1: A lambda function that adds two numbers
add = lambda a, b: a + b
print(add(int(input("Enter first number: ")), int(input("Enter second number: "))))

# Same example using regular function definition
def add(a, b):
    return a + b
print(add(int(input("Enter first number: ")), int(input("Enter second number: "))))

# Example 2: A lambda function without parameters that returns a greeting message
Greet = lambda: "Hello, welcome to python world!"
print(Greet())

# Use cases of lambda functions:
# Using conditional statements in lambda functions:
Number = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(Number(int(input("Enter a number: "))))

# Using List comprehension with lambda functions:
L = [lambda arg=x: arg * 10 for x in range(1, 10)]
for i in L:
    print(i())

# Sorting: Lambda functions can be used as the key argument in sorting functions to specify the sorting criteria.
employees = [
    {"name": "Alice", "salary": 70000},
    {"name": "Bob", "salary": 50000},
    {"name": "Charlie", "salary": 90000}
]
sorted_employees = sorted(employees, key=lambda x: x["salary"])
print(sorted_employees)

# Mapping: Lambda functions can be used with the map() function to apply a transformation to each element in a list.
a = [1, 2, 3, 4, 5]
double = map(lambda x: x * 2, a)
print(list(double))

# Filtering: Lambda functions can be used with the filter() function to filter elements from a list based on a condition.
numbers = [10, 15, 20, 25, 30]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Reducing: Lambda functions can be used with the reduce() function from the functools module to perform a cumulative operation on a list of values.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# Limitations of lambda functions:
# 1. Lambda functions can only contain a single expression, which limits their functionality compared to regular functions that can have multiple statements.
# 2. Lambda functions cannot contain statements such as loops, conditionals, or assignments, which can make them less versatile for complex operations.
# 3. Lambda functions are not reusable and cannot be called multiple times, which can lead to code duplication if the same functionality is needed in multiple places.

# Calculator using lambda functions:
add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else "Cannot divide by zero"
print("Select operation:")
print("1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide")
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input")

# Extending the calculator to handle multiple numbers using reduce function:
from functools import reduce
calculator = { 'add' : lambda *args: reduce(lambda x, y: x + y, args),
               'subtract' : lambda *args: reduce(lambda x, y: x - y, args),
               'multiply' : lambda *args: reduce(lambda x, y: x * y, args),
               'divide' : lambda *args: reduce(lambda x, y: x / y if y != 0 else "Cannot divide by zero", args) }

print("Select operation: 1.Add 2.Subtract 3.Multiply 4.Divide")
choice = input("Enter choice (1/2/3/4): ") 
Numbers = list(map(float, input("Enter numbers separated by space: ").split()))

if choice == '1':
    print(f"Result: {calculator['add'](*Numbers)}")
elif choice == '2':
    print(f"Result: {calculator['subtract'](*Numbers)}")
elif choice == '3':
    print(f"Result: {calculator['multiply'](*Numbers)}")
elif choice == '4':
    print(f"Result: {calculator['divide'](*Numbers)}")
else:
    print("Invalid input")