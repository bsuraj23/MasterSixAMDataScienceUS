import re

# print(re.split(r'\d', 'sonal2kashvi5'))
# print(re.split(r'[,:]', 'apple,banana:cherry,mango'))#splits the string wherever it finds either a comma , OR a colon :.
# print(re.split(r'[A-Z]', 'splitAtCapitals'))
# print(re.split(r'_', 'split_this_string'))
# print(re.split(r'9', '20295-07-15'))
print(re.split(r'\W+', 'Word1,Word2.Word3!$'))


# #Ex1 List of strings
# import re
# print(re.findall(r'\d+', 'I have 3 cats and 12 dogs'))
# # Output: ['3', '12']

print(re.findall(r'\d+', 'There are 3 cats and 4 dogs')) #['3', '4']
print(re.findall(r'[A-Z]', 'Python Is Great')) #['P', 'I', 'G']
print(re.findall(r'colou?r', 'color and colour'))#['color', 'colour']
print(re.findall(r'\b\w{4}\b', 'This text has four word size words'))#['This', 'text', 'four', 'word', 'size']
print(re.findall(r'\s', 'space here and there'))#[' ', ' ', ' ']
print(re.findall(r'\w+', 'List all words here123'))#['List', 'all', 'words', 'here123']
print(re.findall(r'[aeiou]', 'Count vowels in sentence'))#['o', 'u', 'o', 'e', 'i', 'e', 'e', 'e']
