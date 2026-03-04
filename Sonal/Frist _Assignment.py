# ClassNo=3
# name="sonal"
# float=5.7
# print(f'My class number  is {ClassNo} and name is {name} and float value is {float}')


# #List datatype
# fruits=["mango","kivi","banana"]
# print (*fruits)

# #tuple datatype which is immutable
# my_tuple=(1,"sonal",3,4,5,6)
# print(*my_tuple)

# #dictionary datatype which is mutable
# My_dict={"kashvi":8,"vedang":15,"niva":11}
# print(My_dict["kashvi"])  #output=8
# print(My_dict.get("vedang"))  #output=15
# My_dict["sonal"]=45 #adding new key pair value in dictionary
# print(*My_dict.keys())  #output=dict_keys(['kashvi', 'vedang', 'niva']))

# #Python sets are unordered collections of unique, immutable elements.
# print("set datatype")
# name={2,"apple",5,6,5}
# print(type(name)) #output-set datatype
# print(*name)


name="sonal"
print(name.upper()) #output-SONAL
print(name.lower()) #output-sonal
print(name.capitalize()) #output-Sonal 

#print square root of given number without using inbuile finction sqrt() function
i=1
a=int(input("enter any number= "))
while (i<a):
    i=i+1
    if(a==i*i):
       print("The square root of given number is ",i)

#check given password is numeric or alpha without using isalpha()
FLAG=False
password="56sona"
for i in password:
        if (('A' <= i <= 'Z') or ('a' <= i <= 'z') ):
            FLAG=True
        else:
            print("Password is Numeric")
            FLAG=False
            break;

if FLAG==True:
    print("Password contains alphabete letter")


#ASCII value
# A–Z	65–90
# a–z	97–122
# 0–9	48–57

if 'A'<='a':
    print("Uppercase have lower ASCII value")
else:
    print("Lowercase alphbate have larger ASCII value")


#in and not in are membership operators.

numbers = [1,2,3,4,5,6,7]
password="344709"
if all(int(ch) in numbers for ch in password):
    print("All characters are present")
else:
    print("Some characters are missing")