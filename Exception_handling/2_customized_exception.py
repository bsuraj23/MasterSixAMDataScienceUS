# Customized Exception Handling by using try-except
class MyClass(Exception):
    pass
try:
    raise MyClass("Custom error occurred")
except MyClass as e:
    print(e)


#Example of raise
print("----------")
class data(Exception):
    pass
try:
    x=2
    if x<10:
        raise data("Custome error")
except data as e:
    print("Exception Info:",e)


#When to use raise with built‑in exceptions
#To enforce input rules in your functions.
print("--------------")
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    result = set_age(-5)
    print("Age:", result)
except ValueError as e:
    print("Error:", e)


    
