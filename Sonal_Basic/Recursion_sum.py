
#Ex1 Sum with recursive function
def sum_recursive(a, b):
    if b == 0:
        return a  # Base case: when b is 0, return a
    return sum_recursive(a + 1, b - 1)  
print(sum_recursive(10, 3))  # Output: 13


#Ex:2 Sum of all numbers up to the given number.
# def sum_numbers(n):
#     if n == 0:
#         return 0
#     return n + sum_numbers(n-1)
# print(sum_numbers(4)) #output 10

    

