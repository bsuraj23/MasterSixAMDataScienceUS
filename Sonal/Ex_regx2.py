import re
# #Ex1
# pattern = re.compile(r'\d+')                  
# print(pattern.match('123abc'))
# #or
# print(re.match(r'\d+','123abc')) 

# #Ex2
# pattern3 = re.compile(r'^Hello')
# print(pattern3.match('Hello World'))
# #or ^ doesn't require for match , works same
# print(re.match(r'^Hello','Hello World'))

# #Ex3
# pattern4 = re.compile(r'Sonal$')
# print(pattern4.search('TMy name is Sonal'))

#Ex4
pattern5 = re.compile(r'[A-Z]{4,}') #find 4 or more uppercase letters in a row
print(pattern5.search('abCDLKKK123'))

#Ex5
#. matches any character except newline (\n).. matches any character except newline (\n)
pattern6 = re.compile(r'.+')
print(pattern6.match('&sdfd\n'))


