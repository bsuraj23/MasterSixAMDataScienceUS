import re #Regex (regular expression)

# print(re.match(r'\d+', '4dbc'))  # match digit at start
# print(re.match(r'\w+', '&>?')) #1+ alphanumeric
# print(re.match(r'[A-Z]', 'ython3jAshjdsgasgdasudfgdhsss')) #starts uppercase
# print(re.match(r'[a-z]+', 'xYZabc')) #start with lowercase

#^works same like match will search at starting position
print(re.search(r'^\d+', 'abc2xyz'))
print(re.search(r'\d+', 'abc2xyz'))
print(re.search(r'is', 'The black cat is here.'))
print(re.search(r'[a-z]+', 'helloWorldTest')) #First sequence of lowercase
# print(re.search(r'the', 'This is the table')) #will search "the" anywhere
# print(re.search(r'table$', 'This is the table'))#will search at end
# print(re.search(r'\w+', '**&3()')) #will search alphanumeric in entire string
# print(re.search(r'col?our', 'This is nice coour')) #will ignore l and give output
# print(re.search(r'\s', 'vy vyhere'))# matches ANY single whitespace character

