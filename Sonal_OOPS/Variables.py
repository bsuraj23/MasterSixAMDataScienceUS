import math
print(math.pi)  #3.141592653589793
class Demo:   
    # Static variable (class variable)
    """example class for types of variables"""
    static_var = "I am static!" 
    def __init__(self, value):
        # Instance variable
        self.instance_var = value       
    def show(self):
        # Local variable
        local_var = "I am local!"
        print("Instance variable:", self.instance_var)
        print("Static variable:", Demo.static_var)
        print("Local variable:", local_var)
    
srivalli = Demo("I am Srivalli!")
srivalli.show()
print(srivalli.instance_var)  #I am Srivalli!
print(Demo.static_var)        #I am static!
Srilekha = Demo("I am Lekha ")
Srilekha.show()



#Ex of getting documatation of inbuilt function
print(math.sqrt.__doc__)
print(math.cbrt.__doc__)


#Ex: Various Places to declare Static Variables
class Student:
    school = "ABC School"  # Inside class
    def __init__(self):
        Student.school = "XYZ School"  # Inside constructor
    def set_school(self):
        Student.school = "New School"  # Inside method
s1=Student()
print(s1.school)  #XYZ School
s1.set_school()   
print(Student.school)#New School (after calling set_school)




    