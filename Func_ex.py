# Example 6
def multiply_numbers(a, b, c):
   
    return a * b * c
def multiply_numbers(a, b, c, d):
   
    return a * b * c * d
def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply_numbers(2, 3, 4))
print(multiply_numbers(2,  4))
print(multiply_numbers())


# Example with both *args and **kwargs
def greet(*names, **messages):
    for name in names:
        message = messages.get(name, "Hello")
        print(f"{message}, {name}!")
greet("Alice", "Bob", Alice="Hi", Bob="Welcome")