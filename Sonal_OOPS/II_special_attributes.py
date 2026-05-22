#Ex:1 __dict__:Only variables assigned using self. become part of the object and go into __dict__")
print("---"*25)
class Person:
    def __init__(self, name, age):
        x=10              # local variable
        self.name = name  # Stored in __dict__
        self.age = age    # Stored in __dict__

p = Person("Alice", 25)
print(p.__dict__)


#"Ex:2 of __dict__"
print("---"*25)
class Person:
    def __init__(self, items):
        self.items = items   # list stored as value

p = Person([1, 2, 3])
print(p.__dict__)


