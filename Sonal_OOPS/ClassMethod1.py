# you need to work with class data
# You want alternative ways to create objects
# You want your code to support inheritance properly
#Class methods are mainly used to CREATE objects

#Ex1: No object is created if age < 18
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_user(cls, name, age):
        if age < 18:
            return None   # or raise error
        return cls(name, age) #creates a User object here
u1 = User.create_user("sam", 20)   
u2 = User.create_user("rayan", 15)    

print(u1.name)  #sam
print(u2)        # None, means will not create object

#below is alternate way but creating object first that is not actual ask
#we can use instance method in regular way but in that case we have to create object first
class User:
    def create_user(self,name, age):
        self.name=name
        self.age=age
        if self.age < 18:
            return None   # or raise error
        return self.age
obj = User() # must create an object first
result = obj.create_user("Alice", 14) # we just created an object we shouldn’t have
print(result)   



#Ex2
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello {self.name}"

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, age)  # 👈 using cls
class Admin(User):
    pass
u=User.from_string("sonal-40")
print(u.greet())


