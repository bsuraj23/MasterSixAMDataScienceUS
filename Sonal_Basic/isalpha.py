#check given password is numeric or alpha without using isalpha()
FLAG=False
password="56sona"
for i in password:
        if (('A' <= i <= 'Z') or ('a' <= i <= 'z') ):
            FLAG=True
        else:
            print("Password is Numeric")
            FLAG=False
            break;

if FLAG==True:
    print("Password contains alphabete letter")


#ASCII value
# A–Z	65–90
# a–z	97–122
# 0–9	48–57

if 'A'<='a':
    print("Uppercase have lower ASCII value")
else:
    print("Lowercase alphbate have larger ASCII value")
