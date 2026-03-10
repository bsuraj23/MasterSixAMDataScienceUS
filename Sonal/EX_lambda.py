# power = lambda x, y=2: x ** y
# print(power(3))      # Uses default argument y=2, Output: 9
# print(power(2, 3))   # Overrides default argument, Output: 8

# Lambda function with variable-length arguments
# concat = lambda *args:(' '*6).join(args)
# print(concat("Hello","World"))  # Output: Hello World

def add(*args):
    return sum(args)
result = add(1,2,3) #output:6
print(result)
print(add(10, 20, 30,23,12  ))  # Output: 60


