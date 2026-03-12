
from functools import reduce

# user_input = input("Enter numbers separated by space: ")

# numbers = list(map(int, user_input.split()))

# # Filter only even numbers
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# product = reduce(lambda x, y: x * y, even_numbers)

# print("Product of even numbers is:", product)


# from functools import reduce

user_input = input("Enter number sperate with space: ")
numbers = list(map(int, user_input.split()))
print("Numbers is: ",numbers)

# Filter only even numbers

odd_numbers = list(filter(lambda x : x % 2 != 0, numbers))
print("odd numbers is: ",odd_numbers)
product = reduce(lambda x,y : x * y, odd_numbers )

print ("product of odd numbers is : ", product)