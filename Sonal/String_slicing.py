#Example of reverse a string using a for loop without slicing 

s = "Python"
#print(s[::-1])

#First method
# reverse = ''
# for ch in s:
#     reverse = ch+reverse
    
# print(reverse)

#second method

for i in range(len(s)-1, -1, -1):
    print(s[i], end="")


#below code will concatnate string because defalut input datatype is string

# a=input("enter value for a")
# b=input("Enter value for b")
# c=a+b
# print("c",c)