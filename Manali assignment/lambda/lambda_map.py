# Double each number
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

#Output:
[2, 4, 6, 8]


# Convert numbers to strings
nums = [10, 20, 30]
as_strings = list(map(lambda x: str(x), nums))
print(as_strings)

#Output:
['10', '20', '30']


# Get lengths of words
words = ["apple", "banana", "kiwi"]
lengths = list(map(lambda w: len(w), words))
print(lengths)
#Output:
[5, 6, 4]   

# Square each number
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, nums))
print(squares)
#Output:
[1, 4, 9, 16, 25]

# Convert all words to uppercase
words = ["hello", "world"]
uppercased = list(map(lambda w: w.upper(), words))
print(uppercased)
#Output:
['HELLO', 'WORLD']

#- map() applies that lambda to every number in the list.
