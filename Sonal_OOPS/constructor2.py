#example of constructor
# class car:
#     name="BMW"
#     def __init__(self):
#         print(self.name)

# class model:
#     name="coupe"
#     def __init__(temp,*args): #any name can be use instead of self 
#         print(args)   #('SUV', 'van')
#         name="sedan"   #run this without self
#         print(name)
# #obj1=car()  #BMW
# obj2=model("SUV","van") #('SUV', 'van') sedan
# # print(obj2.name) #coupe
# import copy    # Shallow copy
# obj3=copy.copy(obj2)
# print(obj3.name)
    

#Example of reference assignment
# class student:
#     a=90  
#     def name(self):
#         return "sonal"
# obj1=student()
# obj2=obj1    #reference assignment (or aliasing)
# obj1.a=70
# print(obj1.a)
# print(obj2.name())
# print(obj1.name())

#EX WITH shallo COPY
import copy
class Student:
    name = "name"
    #A class/static variable is defined inside the class body, but outside any method
    age = 14  #static(class)  variable
    def display(*args): #or def display(self):
         print(args)      #print(self.name,self.age)
ajay = Student()
vijay= copy.copy(ajay)  # shallow copy
vijay.age=34
print(ajay.age)     #14
print((vijay.age))  #34 


    
