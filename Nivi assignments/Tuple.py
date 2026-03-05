# Simple Tuple Examples

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Tuple with mixed data types
mixed_tuple = (10, "Hello", 3.14, True)
print("Mixed Tuple:", mixed_tuple)

# Accessing tuple elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Tuple slicing
print("Slice [1:3]:", my_tuple[1:3])

# Tuple length
print("Length of tuple:", len(my_tuple))


# Checking if element exists in tuple
if 3 in my_tuple:
    print("3 is in the tuple")


# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Single element tuple (note the comma)
single_tuple = (42,)
print("Single element tuple:", single_tuple)

# Tuple methods
numbers = (1, 2, 3, 2, 4, 2)
print("Count of 2:", numbers.count(2))
print("Index of 3:", numbers.index(3))
