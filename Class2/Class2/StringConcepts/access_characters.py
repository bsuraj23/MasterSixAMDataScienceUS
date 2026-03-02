# statement     = "Python is easy"
# print(statement)  
# print(statement[0])    # P
# print(statement[-1])   # n


s = "Welcome"
print(s[0])
s = "A" + s[1:]
print(s)
print(s[3])
print(s[1:1]) # gives output as empty string

# Negative index starts from right side
print(s[-1])

# string[start:end] --->Access Multiple Characters (Slicing)
print(s[0:3])

# string[start:end:step] --->Skip Characters (Step)
print(s[0:7:2])

# Reverse a String
print(s[::-1])

# Access Last 3 Characters
print(s[-3:])
# Access First 4 Characters
print(s[:4])
#print(s[10]) # string index out of range

print(s[:]) # full copy
print(s[::])


name = "Tejaswini"
print(name[0])

num = "12345"
print(num[-1])