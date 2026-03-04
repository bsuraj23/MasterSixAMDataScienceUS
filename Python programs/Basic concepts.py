# -------------------------------
# 1. Variables and Data Types
# -------------------------------
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Type casting
salary = 50000.50
is_employee = True

print("\n--- Basic Info ---")
print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("Employee:", is_employee)


# -------------------------------
# 2. Conditional Statements
# -------------------------------
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# -------------------------------
# 3. Loops
# -------------------------------
print("\n--- For Loop Example ---")
for i in range(1, 6):
    if i == 3:
        continue  # skip 3
    if i == 5:
        break     # stop loop at 5
    print("Number:", i)

print("\n--- While Loop Example ---")
count = 0
while count < 3:
    print("Count:", count)
    count += 1


# -------------------------------
# 4. Data Structures
# -------------------------------
print("\n--- Data Structures ---")

# List
numbers = [10, 20, 30, 40]
numbers.append(50)

# Tuple
coordinates = (10.5, 20.5)

# Set
unique_numbers = {1, 2, 2, 3, 4}

# Dictionary
person = {
    "name": name,
    "age": age
}

print("List:", numbers)
print("Tuple:", coordinates)
print("Set:", unique_numbers)
print("Dictionary:", person)


# -------------------------------
# 5. Functions
# -------------------------------
def greet(user):
    return f"Hello, {user}!"

print("\n", greet(name))


# Function with *args
def add_numbers(*args):
    return sum(args)

print("Sum:", add_numbers(1, 2, 3, 4))


# Function with **kwargs
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_details(city="New York", country="USA")


# -------------------------------
# 6. List Comprehension
# -------------------------------
squares = [x*x for x in range(5)]
print("\nSquares:", squares)


# -------------------------------
# 7. Lambda Function
# -------------------------------
multiply = lambda a, b: a * b
print("Multiply:", multiply(5, 3))


# -------------------------------
# 8. Exception Handling
# -------------------------------
try:
    num = int(input("\nEnter a number to divide 100: "))
    result = 100 / num
    print("Result:", result)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
finally:
    print("Execution completed.")


# -------------------------------
# 9. File Handling
# -------------------------------
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")

with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFile Content:")
    print(content)