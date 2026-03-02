import math
print(math.ceil(4.2))  # 5 Rounds a number UP to the nearest integer
print(math.floor(4.7)) # 4 Rounds a number DOWN to the nearest integer

print(  math.sqrt(9))  # 3.0  Finds the square root of a number
print(  math.factorial(4)) # 24  Product of all positive integers up to that number

# Square root WITHOUT using predefined functions

n = 36
i = 1

while i * i <= n:
    if i * i == n:
        print("Square root is", i)
        break
    i += 1