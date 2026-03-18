

# *args and **kwargs: Dynamic Duo


# Example 1: *args - sum all numbers
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))

# Example 2: *args - print all arguments
def print_args(*args):
    print(args)

print_args("apple", "banana", "cherry")

#what if the user give nonnumerical arguments, we can fix this by type checking
def add_all_advanced(*args):
    # Filter to ensure we only sum actual numbers
    numbers = [n for n in args if isinstance(n, (int, float))]
    #return sum(numbers) or "Error: Input must contain numbers."
    # Check: Is the length of our "clean" list the same as the "raw" input?
    return sum(numbers) if len(numbers) == len(args) else "Error: Some inputs were not numbers."

print(add_all_advanced(2,3,5,6))
print(add_all_advanced(2,3,"hi",6))

# Example 3: **kwargs - print key-value pairs
def show_kwargs(**kwargs):
    # kwargs is a dictionary: {'name': 'Ram', 'age': 25}
    for key, value in kwargs.items():
        print(f"{key} is {value}")

show_kwargs(name="Ram", major="Math", status="Learning")

#key word arguments **kwargs:

students = {}
def studentInfo(name, **scores): #you can name the key word arguments for ex:**kwargs as **scores (what evert is meaningful for your function)
  students[name] = scores
  return students

studentInfo("Ram", Math = 95, English = 90, Macro = 94)
studentInfo("Sanvi", Math = 90, English = 98, Macro = 92, Bio = 93)
print(students)
