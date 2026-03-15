#in and not in are membership operators.

numbers = [1,2,3,4,5,6,7]
password="344709"
if all(int(ch) in numbers for ch in password):
    print("All characters are present")
else:
    print("Some characters are missing")