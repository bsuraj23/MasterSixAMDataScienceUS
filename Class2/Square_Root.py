# Square root of a numberv using predefined function
import math
number = float(input("Enter a number: "))
if number < 0:
    print("Square root is not defined for negative numbers.")
else:
    print(f"The square root of {number} is {math.sqrt(number)}")

# Square root of a number using user defined function
def square_root(n):
    if n < 0 :
        return "Square root is not defined for negative values."
    elif n == 0 or n == 1:
        return n
    else:
        return n ** 0.5
    
Number = float(input("Enter a number: "))
print(square_root(Number))