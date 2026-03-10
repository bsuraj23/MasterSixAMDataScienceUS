
def toUppercase(func):
    def wrapper():
        mystring = func()
        return mystring.upper()
    return wrapper


@ toUppercase
def say_hello():
    return "hello there"

print(say_hello())