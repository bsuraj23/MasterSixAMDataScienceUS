name = "Tejaswini"
age = 28
print("My name is {} and age is {}".format( age,name))
print(f"My name is {name} and age is {age}")

# code for using int or float,decimal in format
height = 5.5
# print("My name is {} and age is {} and height is {}".format(name, age, height))
# print(f"My name is {name}, age is {age}, and height is {height}")
# print("My name is {0}, age is {1}, and height is {2}".format(name, age, height))
# print("My name is {n}, age is {a}, and height is {h}".format(n=name, a=age, h=height))
# print(f"My name is {name}, age is {age}, and height is {height:.1f}")  # formatted to 1 decimal place
# #print("My name is {}, age is {}, and height is {:.1f}".format(name, age, height))  # formatted to 1 decimal place
# print("My name is {0}, age is {1}, and height is {2:.1f}".format(name, age, height))  # formatted to 1 decimal place
# print("My name is {n}, age is {a}, and height is {h:.1f}".format(n=name, a=age, h=height))  # formatted to 1 decimal place


print("My name is %s and my age is %d" % (name, age)) #old method
print(f"{name:<10} | {age:>5}") #alignment and spacing

x = 10
print(f"{x}{x}") #1010-->not adding it's string formatting

#multiplication table using f strings
num = 4

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


