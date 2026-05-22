#In Python, functions and methods are very similar—they both are blocks of 
# reusable code—but the key difference is where they live and how they’re used.

#A function is defined independently, outside of any class.
#Function → standalone tool
def greet(name):
    print(f"Hello, {name}")
greet("sonal")  #,called directly

#A method is a function that is defined inside a class and is associated with an object.
#tool that belongs to an object
class Person:
    def greet(self,name):
        self.name=name
    def student(self):
        print(f"How are u {self.name}")

obj=Person()
obj.greet("sonal") #called through an object
obj.student()
    



