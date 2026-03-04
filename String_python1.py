
str=input("Enter the string:")
print(f"The entered string is :",str)

for i in str:
    print(i)

print(f"last letter in String",str[-1])
print(f"Sliced String",str[0:3:1])
print(f"Sliced string backwards",str[:0:-1])
# String as array
for x in str:
    print(x)

srch=input("Enter text to search in string")
if srch in str:
    # print(srch," found in the string ",str)
    print(f"{srch} found in the string {str}")
else:
    print(srch," not found in the string ",str)

print("Length of string is ",len(str))
print("Split the string:",str.split(),str.split(" "))

sal=input("Enter the salary")
print(f"The price is {sal} dollars")

txt="Hello\nWorld!!!!"
print(txt)
