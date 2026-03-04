def my_isalpha(s):
    if not s:
       return False
    for char in s:
        # Check if character is between 'a'-'z' or 'A'-'Z'
        if not (('a' <= char <= 'z') or ('A' <= char <= 'Z')):
           return False
    return True
test_str = "Pyhton3"
print(f"Is '{test_str}' alpha? {my_isalpha(test_str)}")   # False (contains '3')  

def my_isdigit(s):
    if not s:
       return False
    for char in s:
        # Check if character is between '0'-'9'
        if not ('0' <= char <= '9'):
           return False
    return True
test_str = "12345"
print(f"Is '{test_str}' digit? {my_isdigit(test_str)}")   # True (all characters are digits)
def my_isspace(s):
    if not s:
       return False
    for char in s:
        # Check if character is a space
        if char != ' ':
           return False
    return True
test_str = "   "
print(f"Is '{test_str}' space? {my_isspace(test_str)}")   # True (all characters are spaces)    
def my_isalnum(s):
    if not s:
       return False
    for char in s:
        # Check if character is between 'a'-'z', 'A'-'Z', or '0'-'9'
        if not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')):
           return False
    return True
test_str = "Python3"
print(f"Is '{test_str}' alphanumeric? {my_isalnum(test_str)}")   # True (contains letters and digits)