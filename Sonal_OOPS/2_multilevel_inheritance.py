#Example of multilevel inheritance
class A:
    a=90
    def func1(self):
        print("This is function 1 from class A")    
class B(A):   #inheriting class A
    def func2(self):
        print("This is function 2 from class B")    
class C(B):   #inheriting class B
    def func3(self):
        print("This is function 3 from class C")
obj = C()
print(obj.a)
obj.func1() #calling class A function   
obj.func2() #calling class B function
obj.func3() #calling class C function
obj1 = B()
obj1.func1() #calling class A function
obj1.func2() #calling class B function
#obj1.func3()  #can not access its child class C 


#This is composition in Python, also called a has-a relationship
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
