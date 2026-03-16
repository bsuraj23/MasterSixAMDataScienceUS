import re

# m = re.search(r'(\d{3})-(\d{2})-(\d{4})', '123-45-6789')
# print(m.group(1), m.group(2), m.group(3))

# m = re.search(r'(\w+) (\w+)', 'Hello World')
# print(m.group(0))  #Hello World
# print(m.group(0),m.group(2)) #Hello World World

# m = re.match(r'(abc)(\d+)', 'abc123')
# print(m.group(0), m.group(2)) #abc 123

# m = re.search(r'(Hello|Hi) (\w+)', 'Hi John')
# print(m.group(1), m.group(2)) #will print hello or Hi and follwed by group2

# m = re.search(r'(favou?rite)', 'Red is my favorite color')
# print(m.group(1)) #will not match for 'u'

# m = re.search(r'(start).*(end)', 'start middle end')
# print(m.group(1), m.group(2)) #start end

# m = re.search(r'(\d{2}):(\d{1})', '12:30 PM')
# print(m.group(1), m.group(2)) #12 3


# print(re.fullmatch(r'\d+', '12345')) #12345
# print(re.fullmatch(r'\w+', 'Python3')) #Python3
# print(re.fullmatch(r'abc', 'abc')) #abc
# print(re.fullmatch(r'[a-z]+', 'hello')) #hello
# print(re.fullmatch(r'[A-Z][a-z]+', 'Python')) #Python
# print(re.fullmatch(r'.+', 'JustText')) #JustText
# print(re.fullmatch(r'colou?r', 'color')) #color

#replace
print(re.sub(r'\d+', 'Om', 'Item 123 costs 456')) #Item Om costs Om
print(re.sub(r'cat', 'dog', 'The cat sat on the mat'))#The dog sat on the mat
print(re.sub(r'\s+', '-', 'replace spaces with dash'))#replace-spaces-with-dash
print(re.sub(r'[^a-zA-Z0-9]', '', 'Remove@#Special!'))#RemoveSpecial
print(re.sub(r'_', ' ', 'split_this_string'))#split this string
print(re.sub(r'(.)(?=\1)', '', 'aabbcc'))  # Remove consecutive duplicates O/p abc
print(re.sub(r'^', 'Start-', 'line')) #Start-line
