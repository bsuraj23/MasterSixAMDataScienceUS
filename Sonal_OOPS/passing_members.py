class A:
    """Passing Members of One Class to Another Class"""
    a=90
    def __init__(self, value):
        self.value = value
    def display(self):
        print("Value is", self.value)
    @classmethod
    def classMethod(cls):
        print("This is class method")

    @staticmethod
    def staticMethod():
        print("This is static method")

obj2 = A(89)
print(obj2.a)
obj2.display()
obj2.classMethod()
obj2.staticMethod()
print(obj2.__doc__)
print(obj2.__new__)
obj2.__class__


class B:
    def __init__(self,no):
        self.no=no
aobj = B("10")
bobj = B(obj2)
print(bobj.no.value)





