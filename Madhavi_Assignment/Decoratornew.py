# calling the decorator from another file   
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before greeting")
        return func(*args, **kwargs)
    return wrapper