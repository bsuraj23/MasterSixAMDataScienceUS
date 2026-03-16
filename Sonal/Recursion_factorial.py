#Ex1 Factorial with Recursion
def fact(no):
    if no==1:
        return 1
    else:
        return no*fact(no-1)
print(fact(4)) 

#Ex2: function with default argument
# def add(x=0,y=0):  
#     c= x + y
#     return c,"Hellow World"
# print(add())  
# print(add(10))  
