s = "Python program"
print("gram" not in s)     # false
print("abc"  in s) # false

s = "Welcome to Python"
print("Python" in s) #True
print("to" not in s) #True

# character level check
print("W" in s)   # True
print("z" in s)   # False

languages = ["python", "java", "c", "c++"]
print("python" in languages) #True
print("go" in languages) #False

days = ("mon", "tue", "wed")
print("mon" in days) #True
print("sat" not in days) #True

ids = {101, 102, 103}
print(102 in ids) #true

student = {"name": "Teja", "age": 25}
print("name" in student) #true

# ---------------------------------------
# String membership check
# ---------------------------------------

text = "Welcome to Python"

if "Python" in text:
    print("Python word is present")
else:
    print("Python word is not present")