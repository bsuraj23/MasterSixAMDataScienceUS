class name:
    def __init__(self,lastnm):
        self.lastnm = lastnm 
        print("My name is : Sonal",self.lastnm)
    a=10
    b=6
obj1=name('verma')
value1=obj1.a
print("id of value1 and object1=",id(value1),  id(obj1))

obj2=name('patel')
value2=obj2.a   #new object pointing to same value
print("id of value2 and object2=",id(value2),  id(obj2)) #will share same memory address with obj1.a

obj3=name('kakkad')
value3=obj3.b #new object with different variable will have different memory address
print("id of value3 and object3=",id(value3),id(obj3))

if(value1 is value2):
   print("true") 
else:
    print("false")
