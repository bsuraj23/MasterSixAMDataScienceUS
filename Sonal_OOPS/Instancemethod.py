class Student:
    def __init__(self, name):
        self.name = name
    #getter method
    def get_name(self):
        return self.name
    # instance method example of declaring instance variable
    def set_age(self, age):
        self.age = age
    def display(self):
        print("Name:", self.name, "Age:", self.age)

vamshi = Student("Vamshi")
print(vamshi.get_name())  # Output: Vamshi
vamshi.set_age(40)
print(vamshi.age)  # Output: 20
vamshi.display()  # Output: Name: Vamshi Age: 20


#declaring instance variable outside the class using object reference variable
obj=Student("john")
obj.age=20  
print(obj.name)  # Output: John
print(obj.age)   # Output: 20   


obj2 = Student("Ajay")
obj2.set_age(24)

print(obj2.name)  # Output: John
print(obj2.age)   # Output: 24  

print(obj.__dict__)  # Output: {'name': 'John'} #Output will be a normal dict of all instance attributes
print(obj2.__dict__)  # Output: {'name': 'Ajay', 'age': 30}

del obj.age  # Deleting instance variable age from obj
del obj2.age  # Deleting instance variable age from obj2

print(obj.__dict__)  # Output: {'name': 'John'}
print(obj2.__dict__)  # Output: {'name': 'Ajay', 'age': 30}

