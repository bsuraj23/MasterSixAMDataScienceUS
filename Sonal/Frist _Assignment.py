ClassNo=3
name="sonal"
float=5.7
print(f'My class number  is {ClassNo} and name is {name} and float value is {float}')


#List datatype
fruits=["mango","kivi","banana"]
print (*fruits)

#tuple datatype which is immutable
my_tuple=(1,"sonal",3,4,5,6)
print(*my_tuple)

#dictionary datatype which is mutable
My_dict={"kashvi":8,"vedang":15,"niva":11}
print(My_dict["kashvi"])  #output=8
print(My_dict.get("vedang"))  #output=15
My_dict["sonal"]=45 #adding new key pair value in dictionary
print(*My_dict.keys())  #output=dict_keys(['kashvi', 'vedang', 'niva']))

#Python sets are unordered collections of unique, immutable elements.
print("set datatype")
name={2,"apple",5,6,5}
print(type(name)) #output-set datatype
print(*name)

#Example of upperand lowercase
name="sonal"
print(name.upper()) #output-SONAL
print(name.lower()) #output-sonal
print(name.capitalize()) #output-Sonal 






