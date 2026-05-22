# you cannot have two __init__ methods (constructor) in the same class; the second one 
# simply overrides the first.
#Ex1
# class Student:
#     def __init__(self, name):
#         print("I am single para")
#         self.name = name
#     def __init__(self, name,age,school):
#         print("I am 3 para")
#         self.name = name
#         self.age=age
#         self.school=school

# obj1 = Student("Vamshi")
# #obj1 = Student("Vamshi",24,"USBATHC")

#you can use below example if you want to use same logic
#Ex2
class Student:
    a = 90
    def __init__(self, name, age=None, school=None):
        if age is None and school is None:
            print("I am single para")
        else:
            print("I am 3 para")
        self.name = name
        self.age = age
        self.school = school

#obj1 = Student("Vamshi")                 # works, “single para”
obj1 = Student("Vamshi", 24, "USBATHC")  # works, “3 para”
print(obj1.name,obj1.age,obj1.school)






