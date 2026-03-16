ClassNo=3
name="sonal"
float=5.7
print(f'My class number  is {ClassNo} and name is {name} and float value is {float}')

# Use [] when creating a list directly.
# Use list() when converting another data type to a list.
#List datatype -mutable
fruits=["mango","kivi","banana"]
fruits.pop() #it will remove last element from list
print (*fruits)
fruits.insert(1,"apple") #will insert apple at index 1 and append will add at last
print (*fruits)


#tuple datatype which is immutable.Tuple note: If a tuple contains a list or set inside, it’s not hashable because it has something mutable inside.
my_tuple=(1,"sonal",3,4,5,6)
print(*my_tuple)



#Python sets are unordered collections of unique, mutable elements.
print("set datatype")
name={2,"apple",5,6,5}
print(type(name)) #output-set datatype
print(*name)

#Example of upperand lowercase
name="sonal"
print(name.upper()) #output-SONAL
print(name.lower()) #output-sonal
print(name.capitalize()) #output-Sonal 






