#Ex1
# class Outer:
#     a=10
#     class Inner:
#         def show(self):
#             print("Inner class method")
# o = Outer()
# i = Outer.Inner()
# print(o.a)
# i.show()

#Ex2
class A:
    var =90
    def function(self):
        print("Outer class method")
        self.w=89
    class B:
        def show(self):
            self.a=70
            print("Inner class method")

obj1 = A() # a can not access by obj1
obj2 = A.B()  #var and w are not accessible by obj2

obj2.show() #Inner class method
print(obj2.a) #70    

obj1.function() #Outer class method
print(obj1.w) #89
print(A.var)