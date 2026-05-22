#special attributes (also known as magic attributes, dunder attributes, or
#  double-underscore attributes

class user():
    x=10
    def name(self,name):
        print(f"my name is{name}")
class child(user):
    y=10
    pass
obj=user()
obj.name("John")


print("Ex:1__base__:   refers to the immediate parent class")
print("---"*25)
print(user.__base__)  #<class 'object'>
print(child.__base__)  #<class '__main__.user'>


print("Ex:2: Example of __base__")
print("---"*25)
class A:
    pass
class B:
    pass
class C(A, B):  # Inherits from A and B
    pass
print(C.__base__)  # <class '__main__.A'> (first base class)
print(C.__bases__) # (<class '__main__.A'>, <class '__main__.B'>) (ALL base classes)


print("Ex:3 __class__:returns the class/type to which an object instance belongs")
print("---"*25)
print(user.__class__)        ##<class 'type'>
print(child.x.__class__)    #<class 'int'>
print(obj.name.__class__)   #<class 'method'>


print("Ex:4 __module__: tells you which module (file) an object, class, or function was defined in")
print("---"*25)
print(user.__module__)  #__main__



