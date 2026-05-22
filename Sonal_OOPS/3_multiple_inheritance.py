#code for multiple inheritance concept
#In case of multiple inheritance, Python follows the C3 linearization algorithm to determine the method
# class A:
#     def func1(self):
#         print("This is function 1 from class A")
# class B:
#     def func1(self):
#         print("This is function 2 from class B")
# class C(A, B):
#     def func3(self):
#         print("This is function 3 from class C")
# obj = C()
# obj.func1() #calling class A function
# obj.func1() #calling class B function
# obj.func3() #calling class C function
# obj2 = B()  
# obj2.func1() #this will give error as class B object cannot access class A function

# Diamond Problem Example.MRO: Method Resolution Order
class X:
    def func(self):
        print("Function from class X")

class Y(X):
    def func(self):
        print("Function from class Y")

class Z(X):
    def func(self):
         print("Function from class Z")
class W(Y,Z):
    pass    

# Create object of W and call func 
obj_w = W()
obj_w.func()  
# Show MRO
print("MRO for class W: ", W.__mro__)
#you can call explicitly as below
Z.func(obj_w) #Function from class Z
X.func(obj_w)  #Function from class X 


#once Python finds func in Y, it never goes further into Z or X. The MRO is 
#not a “call all” list; it’s just the search path, and as soon as a matching 
# method is found, the search stops.


