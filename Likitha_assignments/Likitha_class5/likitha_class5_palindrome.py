str="madam"
new=''
for s in str:
    new=s+new
print(new)
if str==new:
  print("palindrome")
else:
  print("not palindrome")