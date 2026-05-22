#Ex1
var = 90
def change():
    var=1
    print(var) #1
change()  
print(var)  #90

# Ex2 
var = 20
def change():
    global var
    var=200   #Modifying inside function (global REQUIRED)
    print(var)  #   change the indentation of this line and see the value
change()  
print(var)  



