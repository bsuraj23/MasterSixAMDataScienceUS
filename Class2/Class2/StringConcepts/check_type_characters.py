#In Python, we usually use string checking methods like:
#isalpha(), isdigit(), isalnum(), isspace(), islower(), isupper()

s = "Python"
print(s.isalpha()) #Check if all characters are letters

a = "Python12"
print(a.isdigit()) #Check if all characters are digits
print(a.isalnum()) #Letters + digits (no spaces or symbols)

s = "   "
print(s.isspace()) #Only spaces / tabs / new lines

s = "python"
print(s.islower()) #All lowercase letters
print(s.isupper()) #All uppercase letters

s = "Welcome To Python"
print(s.istitle())