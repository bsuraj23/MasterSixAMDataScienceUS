# Set - A collection of Unordered, Unchangeable, 
# Unindexed Mutable items

# Creating a set
Myset={"Java","Python","Mainframes","ML"}
print(Myset)

# Creating using set() constructor
Myset = set((1,2,37,9,11))
print(Myset)
print("The Datatype is",type(Myset))

# Creating set with different datatypes
Myset={1,3,5,7,"Odd",78.90345,False}
print(Myset)

#T16- Throws an error as I included list in a set, Lists are unhasable
# Hashable - Doesn't use key to locate the specified item. 
# Hashinh is used for fast data lookup
#Myset={1,4,False,"String",3.678901,[8,4,7]}
#lists and Dictionaries cannot be elements of set as they are not hasable
#Myset={1,5,7,True,{"name":"Andrea","age":50},356.789}
#print(Myset)

#The hash value is usually a number that represents the original 
# data and is used for fast searching and storing.

#No duplicates allowed - Duplicates will be removed automatically
Myset={1,3,5,7,9,11,3,21}
print(Myset)

# Boolean False means 0, so False is removed while 0 in tuple is allowed
Myset={0,10,"Hello",78.098,1,'a',False,(0,2,4)}
print(Myset)
print("Length of the set :",len(Myset)) #Length =7

# Creating empty set
Empty_set={}
print(f"Created set is of type {type(Empty_set)}") #creates dictionary

Empty_set=set()
print(f"Created set is of type {type(Empty_set)}")

#How to access Set
for i in Myset:
    print(i)

chk=input("Enter a item to check if it exist in the Set: ")
chk1=int(input("Enter a non-string item to check if it exist in the Set: "))

#Returns true if chk is a string, default is string
if chk in Myset or chk1 in Myset:
    print(f"Item exists in the set {Myset}")
else:
    print(f"Item doesn't exist in the set {Myset}")
