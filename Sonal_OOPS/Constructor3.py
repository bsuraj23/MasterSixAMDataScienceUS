# instance method example of declaring instance variable
class Student:
    a=10
    # def __init__(self, name):
    #     print("I am single para")
    #     self.name = name
    def __init__(self, name,age):
        print("I am 3 para")
        self.name = name
        self.age=age
    
    def set_age(self,name,age,no): 
        self.age=age
        
        self.no=no #any instance method can add new attributes to self at any time
        return self.name,self.a,self.no
    def display(self):
        print("Name:", self.name) #passing age but not displaying
#obj1 = Student("Vamshi")
obj1 = Student("Vamshi",30)
obj1.display()
print(obj1.set_age("sonal",50,40))
obj1.display()

