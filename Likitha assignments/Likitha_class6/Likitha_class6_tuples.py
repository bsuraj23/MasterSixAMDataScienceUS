#Tuple: An ordered, immutable collection of elements that allows duplicates and can store heterogeneous data types.
#Different ways to create a tuple:
#1. Using parentheses
my_tuple = (1, 2, 3, 'Hello', 3.14)
print(my_tuple) 

#2. Using the tuple() constructor
my_tuple2 = tuple([4, 5, 6, 'World', 2.71])
print(my_tuple2)            
#3. Single element tuple (note the comma)
t1 = (42,) #Without the comma, it would be considered an integer, not a tuple
print(t1)   

#Accessing tuple elements
my_tuple = (1, 2, 3, 'Hello', 3.14)
print(my_tuple[0])  #
print(my_tuple[3])  
print(my_tuple[-1]) 
print(my_tuple[1:4])
print(my_tuple[:3])
print(my_tuple[2:])



#Concatenating tuples
concatenated_tuple = my_tuple + my_tuple2
print(concatenated_tuple)

#Repeating tuples
repeated_tuple = my_tuple * 2
print(repeated_tuple)

#Tuple unpacking
my_tuple = (1, 2, 3, 'Hello', 3.14)
a, b, c, d, e = my_tuple
print(a)  # Output: 1
print(d)  # Output: 'Hello'
print(e)  # Output: 3.14
#Tuples are immutable, so you cannot change their elements
#my_tuple[0] = 10  # This will raise a TypeError

#methods for tuples
t = (1, 2, 3, 2, 4)
print(t.count(2)) # Output: 2
print(t.index(3)) # Output: 2   


# memebership testing
t = (10, 20, 30)
print(20 in t)  # True
print(50 not in t) # True

#built-in functions for tuples
t = (1, 2, 3, 4)
print(len(t)) #length of tuple
print(min(t)) #`minimum value in tuple`
print(max(t)) #`maximum value in tuple`
print(sum(t)) #`sum of all elements in tuple`

# List in tuple
t = (1, 2, [3, 4])
t[2][0] = 100
t[1]=4
print(t) #Output: (1, 2, [100, 4])

# conversion of tuple to list
t = (1, 2, 3)
l = list(t)
print(l) #Output: [1, 2, 3]

# conversion of list to tuple
l = [4, 5, 6]
t = tuple(l)
print(t) #Output: (4, 5, 6)

#nested tuples
t = ((1, 2), (3, 4), (5, 6))

print(t[1])
print(t[1][0]) #Output: 3
