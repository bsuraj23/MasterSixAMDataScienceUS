
def greet():
    print("Hi..I am Kiran")

def call_function(func):
    func()

call_function(greet)

def my_decorator(func):

    def wrapper():
        print("Hi running program before the function")
        func()
        print("Hello.. Program runs after the functiom")

    return wrapper

@my_decorator
def call_to_say_hello():
    print("Hellooooo")   

#call_to_say_hello = my_decorator(call_to_say_hello) 
call_to_say_hello()  
