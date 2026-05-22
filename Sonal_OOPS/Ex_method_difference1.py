class A:
    x = 10
    def __init__(self, y):#always takes object value 
        self.y = y
    def instance_method(self): 
        return  self.y +self.x
    @classmethod
    def class_method(cls):
        return cls.x
    @staticmethod
    def static_method():
        return A.x
class B(A):
    x = 20
b = B(5)
print(b.instance_method())
print(B.class_method())
print(B.static_method())