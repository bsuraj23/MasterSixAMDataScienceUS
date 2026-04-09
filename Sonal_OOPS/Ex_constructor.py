#eample of constructor
class car:
    name="BMW"
    def __init__(self):
        print(self.name)
obj1=car()
class model:
    name="coupe"
    def __init__(temp,*args): #any name can be use instead of self 
        print(args)
        print(temp.name)
obj2=model("SUV","van")
print(obj2.name)
    

#Ex of self
# class student:
#     a=90
#     def name(self):
#         return "sonal"
# obj1=student()
# print(obj1.name())
    
    
