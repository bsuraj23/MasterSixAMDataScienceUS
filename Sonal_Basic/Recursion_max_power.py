# Ex: Give power of given number
# def power(base, exp):
#     if exp == 0:
#         return 1
#     return base * power(base, exp - 1)
# print(power(2, 4))

#Ex find the maximum value with recursion
def find_max(a):
    if (len(a)==1):
        return a[0]
    return max(a[0], find_max(a[1:]))
        
print(find_max(['3','6','2','4']))

# find the GCD (greatest common divisor) using recursion.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(48, 18)) #Op 6

