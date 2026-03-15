#Example of reverse a string using slicing 
s = "Python"
print(s[::-1])

def reverse(s):
    return s[::-1]
print(reverse("Hello"))

#Example of reverse a string using a for loop without slicing
reverse = ''
for ch in s:
    reverse = ch+reverse
print(reverse)


#Example of reverse string
s="Monal"
for i in range(len(s)-1, -1, -1):
    print(s[i], end="")  #end="" replaces it with empty string ,chars print on same line


