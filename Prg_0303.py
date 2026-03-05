# Code without using in

str=input("Enter a string: ")
charc=input("Enter a character to search: ")
sucess=False

for i in str:
    if charc==i:
        print(f"{charc} found in {str}")
        sucess=True
        break

if sucess == False:
    print(f"{charc} not found in {str}")