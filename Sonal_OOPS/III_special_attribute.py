#Example 1:__doc__  is useful for writing readable code and for generating help text"
print("---"*25)

class User:
    """User class for managing user data."""
    
    def __init__(self, name: str, age: int):
        """Initialize User with name and age."""
        print(self.__init__.__doc__)
        self.name = name
        self.age = age
       
user = User("Alice", 25)
print(User.__doc__)
print(User.__init__.__doc__)


#Example :2 __init_subclass__"
print("---"*25)
class Base:
    def __init__(self):
        print("__init__ - object created")
    
    def __init_subclass__(cls):
        print("__init_subclass__ - class defined from",cls.__name__)

class Dog(Base): pass  # Runs here (class definition)
dog1 = Dog()           # Runs here (object creation)  
dog2 = Dog()           # Runs AGAIN (another object)




