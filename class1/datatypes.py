print("Different data types for Python")

b = True
print("value of b is ", b)
print(type(b))

a = 89
b = 454545454
c = 34.56656565

print("value of b is " + str(b))

#Tejaswinich Homework

#int
a = 0
b = 21
c = -1
d = 9087656
age = 22

print(type(c))  # <class 'int'>

#string
name = "Teja"
b = "3211"
c = "Python"
d = "Hello World"

print(type(b))   # <class 'str'>

#Float
a = 3.14
Height = 5.5
b = -2.5
c = 0.0

print(type(b))   # <class 'float'>

#Boolean
a = True
b = False
c = 10 > 5        # True
d = 3 == 4        # False
e = bool(1)       # True
print(e)
print(type(e))   # <class 'bool'>

#List  -->Ordered collection, mutable (can change)
a = [1, 2, 3]
b = ["apple", "banana", "mango"]
c = [1, "Python", True]
d = []
e = [10, 20, 30, 40, 50]
print(d)
a.append(4)
print(a)
print(type(d))   # <class 'list'>


#Tuple  ---> Ordered collection, immutable (cannot change)
a = (1, 2, 3)
b = ("red", "blue", "green")
c = (10, "AI", True)
d = ()
e = (100,)
print(type(a))   # <class 'tuple'>
