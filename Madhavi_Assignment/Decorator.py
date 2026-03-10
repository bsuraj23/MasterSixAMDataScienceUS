# A decorator is something that adds extra behavior to a function without changing the function itself.

#Example - A Company app has a page to view employee salaries
# First check if user is logged in or not. if user is logged in then only allowd to see the salaries page.
def my_decorator(func):
    def wraffer():
        print("Checking if user is loggedin or not")
        func()
        
    return wraffer
@my_decorator
def view_salary():
    print("Showing salary detailsof employees")

view_salary()

# More examples
# Goal is print message before function run
def before_message(func):
    def wrapper1():
        print("Printing message before main function runs")
        func()
    return wrapper1
#@before_message
#def greet():
#print("Hello")
#greet()

#run the decorator without using @ symbol
def another_grret():
    print("Checking without @symbol  " + "Hi there")

another_grret=before_message(another_grret)
another_grret()

#Decorator with Arguments
def decorator_with_arguments(func):
    def wrapper(name):
        print("This is a decorator with arguments")
        func(name)
    return wrapper
@decorator_with_arguments
def greet(name):
    print("Hi there, " + name)
greet("Madhavi")

#More Examples on Decorator passing argument at the runtime using input 
def decorator_with_arguments(func):
    def wrapper(name):
        print("This is a decorator with arguments")
        func(name)
    return wrapper
@decorator_with_arguments
def greet(name):
    print("Hi there, " + name)
name= input("Enter your name: ")
greet(name)

# Decorator with multiple arguments
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before greeting")
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def greet(name,city):
    print("Hello ,", name, "Lives in", city)

name= input("Enter your name ")
city= input("Enter your City ")

greet(name,city)

# Execution flow
'''
Program start
      ↓
Decorator defined  (my_decorator) 
      ↓
wrapper defined (wraper is created inside decorator function)
      ↓
@my_decorator applied   (main function is decorated with my_decorator function)
      ↓
greet = my_decorator(greet) (greet function is passed as an arguments to my_decorator function and wrapper function is returned and assigned to greet)
      ↓
User input taken    (enter name & city during runtime  )
      ↓
greet(name,city) ( greet function is called with arguments name and city)
      ↓
wrapper(name,city) (wrapper function is executed with arguments name and city)
      ↓
print("Before greeting") (First line of wrapper function is executed and message is printed)
      ↓
original greet(name,city) (function is called with arguments name and city)
      ↓
print greeting message (original function runs ) '''