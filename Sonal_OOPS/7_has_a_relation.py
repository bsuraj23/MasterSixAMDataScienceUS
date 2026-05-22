#This is composition in Python, also called a has-a relationship(also called composition or aggregation)
#Composition: Strong ownership
class A:
    def func_A(self):
        print("This is function A from class A")    
class B:
    def func_B(self):
        print("This is function B from class B")    
class C:
    def __init__(self):
        self.a = A()  # class C has a relationship with A
        self.b = B()  # class C has a relationship with B
    def func_temp(self): 
        print("Calling function temp through instance attribute")
        self.a.func_A() 
        self.b.func_B() 
obj = C()
obj.func_temp()



## Aggregation: Weak ownership
class A:
    def func_A(self):
        print("This is function A from class A")    
class B:
    def func_B(self):
        print("This is function B from class B")    
class C:
    def __init__(self,a_obj: A, b_obj: B):
        self.a = a_obj  # class C has a relationship with A
        self.b = b_obj  # class C has a relationship with B
    def func_temp(self): 
        print("Calling function temp through instance attribute")
        self.a.func_A() 
        self.b.func_B() 
a=A()
b=B()
obj = C(a,b)
obj.func_temp()