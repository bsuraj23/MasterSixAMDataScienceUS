#So cyclic inheritance is not a valid inheritance pattern; it’s a logical 
#error you should avoid by making sure that your parent‑class declarations never form a loop.


#code for cyclic inheritance concept
class A(B): pass
class B(A): pass

#code for cyclic inheritance concept with functions
class A(B):
    def funcA(self):
        print("Function A")
class B(A):
    def funcB(self):
        print("Function B")