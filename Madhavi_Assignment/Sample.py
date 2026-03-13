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

