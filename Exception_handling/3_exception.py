# Default except Block
try:
    x = 1 / 0
except:
    print("Some error occurred")


# else Block with try-except-finally
print("--------------")
try:
    x = 10
except:
    print("Except")
else:
    print("Else block")
finally:
    print("Finally block")

# Python's Exception Hierarchy
# BaseException > Exception > ArithmeticError, LookupError, etc.

print("-------------")
print(Exception.__mro__)