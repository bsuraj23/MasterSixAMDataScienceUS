import re
#Ex1 Iterator of Match objects
# list =[]
# for i in re.finditer(r'\d+', 'Item1 Item2 Item3 456 Item4 7890'):
#     list.append(i.group())
# print(list) #['1', '2', '3', '456', '4', '7890']

# matches = re.finditer(r'\d+', 'Item 1 costs 20 and 30 more')
# for m in matches:
#     print(m.group()) #1 20 30

# matches = re.finditer(r'\w+', 'List all words here')
# for m in matches:
#     print(m.group()) #List all words here

matches = re.finditer(r'[A-Z]', 'Python Is Powerful')
for m in matches:
    print(m.group()) #P I P

matches = re.finditer(r'colou?r', 'color or colour appears twice')
for m in matches:
    print(m.group()) #color colour

matches = re.finditer(r'\b\w{3}\b', 'One two orange blue red')# will take only three letters word
for m in matches:
    print(m.group())

matches = re.finditer(r'\s', 'Multiple spaces exist here')
for m in matches:
    print('Space found at:', m.start())

matches = re.finditer(r'\d{2}', '12 34 565 78') #12 34 56 78
for m in matches:
    print(m.group())