import math
from decimal import Decimal

print(math.floor(4.777)) # output: 4

# a=input("Enter any float value a= ")
# b=input("Enter any value b= ")

# Total=float(a)+float(b)
# print("Total= ", float(Total)) #computer sums float as binary so comes with long number
# #print("Total= ", round(Total)) 

# print("Total=",round(Total,3)) #rounding to 2 decimal places

#In Python, float is actually a double-precision floating-point number under the hood.

a = Decimal('0.1')
b = Decimal('0.2')
total = a + b
print(total)  # 0.3
