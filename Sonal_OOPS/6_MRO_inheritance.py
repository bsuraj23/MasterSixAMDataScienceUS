#MRO
# super() gives you a temporary object that lets you call methods from the
# parent class of the current class.
class A: pass
class B(A): pass
class C(B): pass
print(C.mro())

#super function
class X:
    def func(self):
        print("This is function from class X")

class Y(X):
    def func(self):
        super().func()
        print("This is function from class Y")

class Z(Y):
    def func(self):
        super().func()
        print("This is function from class Z")
        

# obj = Z()
# obj.func()  #calling class Z function which will call super class function

obj1 = Y()
obj1.func() #calling class Y function which will call super class function  

