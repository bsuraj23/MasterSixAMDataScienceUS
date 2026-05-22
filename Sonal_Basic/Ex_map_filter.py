#Apply a function to every item in an iterable (like a list) and return a new iterable.
#map(function, iterable)
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

def even(x):
    if x%2==0:
        return x
user_inputs = [1, 2, 3, 4, 5]
squared_values = list(map(even, user_inputs))
print(squared_values)  #if False → return None


#Keep only the items that satisfy a condition (for which the function returns True).
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

words = ["apple", "banana", "cherry", "date"]
a_words = list(filter(lambda word: word.startswith('a'), words))
print(a_words)



#Repeatedly apply a function to combine the items of an iterable into one value (sum, product, etc.).
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

def multiply(x, y):
    return x * y
result = reduce(multiply, [1, 2, 3, 4])
print(result)  # Output: 24 (1*2*3*4)









