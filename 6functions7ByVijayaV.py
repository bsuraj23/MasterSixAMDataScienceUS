
# function that counts the freequency of each word in a sentence
def word_frequency(text):
  # .lower() ensures "Python" and "python" are counted as the same word
  # .split() breaks the string into a list based on whitespace
    line = text.lower().split()
    freq = {}
    for word in line:
        freq[word] = freq.get(word, 0) + 1
    return freq

sentence = "Python is fun python"
print(word_frequency(sentence))



# #variable length args
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply(1, 2, 3))        # Output: 6
print(multiply(4, 5))           # Output: 20


# or use prod() function in math library to make your code more concise and avoid reinventing the wheel

import math # need prod()function in math library to find the product of a list of numbers
#  #Function that gives product of numbers in a list
def productOfNnums(*args):
  print(f"Product of {args} is {math.prod(args)}")

productOfNnums(1,2,3,4)



