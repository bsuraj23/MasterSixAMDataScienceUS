#Method Overloading using *args (simulated overloading).

class MathOperations:
    def __init__(self, a, b):
       self.a = a
       self.b = b
       self.c = 0
       print("Two arguments constructor called")
   
    def __init__(self, a):
       self.a = a
       self.b = 0
       self.c = 0
       print("One argument constructor called")
    def __init__(self):
         self.a = 0
         self.b = 0
         self.c = 0
         print("No arguments constructor called")
    def __init__(self, *args): #variable length arguments
       print("type of args:", type(args))
       print("Variable Length arguments constructor called")
    def add(self,*args):
       return sum(args)
    
math_ops1 = MathOperations()
print(math_ops1.add(1,2,3))  # three arguments

math_ops2 = MathOperations()
print(math_ops1.add(5,6))

#Another example of method overloading with *args and *kwargs
class MathOperations:
    def add(self, a, b, c):
        return a + b + c
    def add(self, a, b, c, d):
        return a + b + c + d
    def add(self, a, b, c, d, e):
        return a + b + c + d + e

math_ops = MathOperations()
print(math_ops.add(5, 10, 15, 40,20)) #will call last method     
# Note: In Python, the last defined method will override the previous ones.

#code for *args method overloading
class MathOperationsVarArgs:
    def add(self, *args):
        return sum(args)    
math_ops_var = MathOperationsVarArgs()
print(math_ops_var.add(5, 10))                # Two arguments   
print(math_ops_var.add(5, 10, 15))            # Three arguments
print(math_ops_var.add(5, 10, 15, 20))        # Four arguments
print(math_ops_var.add(5, 10, 15, 20, 25))    # Five arguments

 