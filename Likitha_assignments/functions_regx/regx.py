#match() function is used to check if the beginning of a string matches a specified pattern. It returns a match object if the pattern is found at the beginning of the string, otherwise it returns None.
import re

print(re.match(r'[A-Z]', 'Python3ajshjdsgasgdasudfgdhsss'))
print(re.match(r'[a-z]+', 'XYZabc'))

print(re.match(r'\d+', '123abc'))
print(re.match(r'\d+', 'abc123'))

print(re.match(r'[A-Z][a-z]+', 'HelloWorld'))
print(re.match(r'[A-Z][a-z]+', 'helloWorld'))

print(re.match(r'\w+', 'Python_123'))
print(re.match(r'\w+', '***Python'))

print(re.match(r'\s+', '   hello'))
print(re.match(r'\s+', 'hello   '))

print(re.match(r'.+', 'Anything'))
print(re.match(r'[a-z]{3}', 'abcXYZ'))

print(re.match(r'[A-Z]{2}', 'ABcd'))
print(re.match(r'[A-Z]{2}', 'Abcd'))

print(re.match(r'hello', 'hello world'))

#search() function is used to search for a specified pattern anywhere in a string. It returns a match object if the pattern is found, otherwise it returns None.


print(re.search(r'[A-Z]', 'pythonIsPowerful'))
print(re.search(r'[a-z]+', 'XYZabc'))

print(re.search(r'\d+', 'abc123xyz'))
print(re.search(r'\d+', 'no digits here'))

print(re.search(r'world', 'Hello world'))
print(re.search(r'Python', 'I love Python programming'))

print(re.search(r'[A-Z]{2}', 'abCDxy'))
print(re.search(r'[A-Z]{2}', 'abcdef'))

print(re.search(r'\s+', 'Hello   World'))
print(re.search(r'\s+', 'HelloWorld'))

print(re.search(r'end$', 'This is the end'))
print(re.search(r'^Start', 'Start here'))

print(re.search(r'\bcat\b', 'A cat is sleeping'))
print(re.search(r'\bcat\b', 'concatenate'))

print(re.search(r'colou?r', 'The color is nice'))

#findall() function is used to find all occurrences of a specified pattern in a string. It returns a list of all matches found.

print(re.findall(r'\d+', 'Item 1 costs 20 and 300'))
print(re.findall(r'\w+', 'List all words here'))

print(re.findall(r'[A-Z]', 'Python Is Powerful'))
print(re.findall(r'[a-z]', 'ABCdefXYZ'))

print(re.findall(r'\b\w{3}\b', 'One two red blue'))
print(re.findall(r'\d{2}', '12 34 567 89'))

print(re.findall(r'[aeiou]', 'education'))
print(re.findall(r'\s', 'A B C D'))

print(re.findall(r'colou?r', 'color colour colors'))
print(re.findall(r'\b[A-Z][a-z]+\b', 'Hello world From Python'))

print(re.findall(r'\w{4}', 'This code works well'))
print(re.findall(r'[^aeiou\s]', 'hello world'))

print(re.findall(r'\b\d+\b', 'Room 101, floor 2, code A7'))
print(re.findall(r'[A-Z]{2,}', 'AB cd EFG hijk LMN'))

print(re.findall(r'.', 'abc'))

#finditer() function is used to find all occurrences of a specified pattern in a string and returns an iterator yielding match objects for each match found.
matches = re.finditer(r'\d+', 'Item 1 costs 20 and 300')
for m in matches:
    print(m.group())

matches = re.finditer(r'\w+', 'List all words here')
for m in matches:
    print(m.group())

matches = re.finditer(r'[A-Z]', 'Python Is Powerful')
for m in matches:
    print(m.group())

matches = re.finditer(r'\b\w{3}\b', 'One two red blue')
for m in matches:
    print(m.group())

matches = re.finditer(r'\s', 'A B C D')
for m in matches:
    print(m.start())

matches = re.finditer(r'\d{2}', '12 34 56 78')
for m in matches:
    print(m.group())

matches = re.finditer(r'[aeiou]', 'education')
for m in matches:
    print(m.group(), m.start())

matches = re.finditer(r'colou?r', 'color and colour')
for m in matches:
    print(m.group())

matches = re.finditer(r'[A-Z]{2,}', 'AB cd EFG hijk LMN')
for m in matches:
    print(m.group())

matches = re.finditer(r'\b[A-Z][a-z]+\b', 'Hello From Python World')
for m in matches:
    print(m.group())

    #fullmatch() function is used to check if the entire string matches a specified pattern. It returns a match object if the whole string matches the pattern, otherwise it returns None.

print(re.fullmatch(r'\d+', '12345'))
print(re.fullmatch(r'\d+', '123abc'))

print(re.fullmatch(r'[A-Z][a-z]+', 'Hello'))
print(re.fullmatch(r'[A-Z][a-z]+', 'Hello123'))

print(re.fullmatch(r'\w+', 'Python_123'))
print(re.fullmatch(r'\w+', 'Python 123'))

print(re.fullmatch(r'[a-z]{3}', 'abc'))
print(re.fullmatch(r'[a-z]{3}', 'abcd'))

print(re.fullmatch(r'\d{2}:\d{2}', '12:30'))
print(re.fullmatch(r'\d{2}:\d{2}', '12:30 PM'))

print(re.fullmatch(r'colou?r', 'color'))
print(re.fullmatch(r'colou?r', 'colour'))

print(re.fullmatch(r'[A-Z]{2,}', 'ABC'))
print(re.fullmatch(r'[A-Z]{2,}', 'AbC'))

print(re.fullmatch(r'.+', 'Hello'))

#re.split() Splits a string using a regex pattern.

import re

print(re.split(r'\s+', 'Split this sentence now'))
print(re.split(r',', 'a,b,c,d'))

print(re.split(r'\d+', 'abc123xyz456test'))
print(re.split(r'[aeiou]', 'education'))

print(re.split(r'\W+', 'Hello@World#Python'))
print(re.split(r'-', '2024-06-15'))

print(re.split(r'\.', 'www.google.com'))
print(re.split(r':', '12:30:45'))

print(re.split(r'\s', 'A B C D'))
print(re.split(r'[A-Z]', 'PythonIsPowerful'))

print(re.split(r'[,:;]', 'one,two:three;four'))
print(re.split(r'\b', 'hello world'))

print(re.split(r'\d{2}', 'ab12cd34ef56'))
print(re.split(r'colou?r', 'startcolormiddlecolourend'))

print(re.split(r'_', 'data_science_python'))

#sub() function `replaces occurrences of a pattern with a specified replacement string.`

import re

print(re.sub(r'\d+', '#', 'abc123xyz456'))
print(re.sub(r'\s+', '-', 'Hello   World   Python'))

print(re.sub(r'[aeiou]', '*', 'education'))
print(re.sub(r'\w+', 'WORD', 'Replace each word here'))

print(re.sub(r'\d', 'X', '12345'))
print(re.sub(r'cat', 'dog', 'cat and cat'))

print(re.sub(r'\s', '_', 'A B C D'))
print(re.sub(r'\w{3}', '###', 'one two red blue'))

print(re.sub(r'[A-Z]', '!', 'HELLO'))
print(re.sub(r'end$', 'finish', 'This is the end'))

print(re.sub(r'^Start', 'Begin', 'Start here now'))
print(re.sub(r'colou?r', 'shade', 'color and colour'))

print(re.sub(r'\b\w{4}\b', 'FOUR', 'This code runs well'))
print(re.sub(r'[^a-zA-Z0-9\s]', '', 'Hello@World#2026!'))

print(re.sub(r'\d{2}', 'YY', '12 34 56 78'))
#subn() function is similar to sub(), but it also returns the number of replacements made.


print(re.subn(r'\d+', '#', 'abc123xyz456'))
print(re.subn(r'\s+', '-', 'Hello   World   Python'))

print(re.subn(r'[aeiou]', '*', 'education'))
print(re.subn(r'\w+', 'WORD', 'Replace each word here'))

print(re.subn(r'\d', 'X', '12345'))
print(re.subn(r'cat', 'dog', 'cat and cat'))

print(re.subn(r'\s', '_', 'A B C D'))
print(re.subn(r'\w{3}', '###', 'one two red blue'))

print(re.subn(r'[A-Z]', '!', 'HELLO'))
print(re.subn(r'end$', 'finish', 'This is the end'))

print(re.subn(r'^Start', 'Begin', 'Start here now'))
print(re.subn(r'colou?r', 'shade', 'color and colour'))

print(re.subn(r'\b\w{4}\b', 'FOUR', 'This code runs well'))
print(re.subn(r'[^a-zA-Z0-9\s]', '', 'Hello@World#2026!'))

print(re.subn(r'\d{2}', 'YY', '12 34 56 78'))
# compile() function is used to compile a regex pattern into a regex object, which can be reused for matching. This can improve performance if you need to use the same pattern multiple times.



pattern = re.compile(r'\d+')
print(pattern.search('abc123xyz'))

pattern = re.compile(r'[A-Z]')
print(pattern.search('pythonIsPowerful'))

pattern = re.compile(r'\w+')
print(pattern.match('Python_123'))

pattern = re.compile(r'^Hello')
print(pattern.match('Hello World'))

pattern = re.compile(r'end$')
print(pattern.search('This is the end'))

pattern = re.compile(r'[A-Z]{4,}')
print(pattern.search('abCDLKKK123'))

pattern = re.compile(r'.+')
print(pattern.match(' '))

pattern = re.compile(r'^\d')
print(pattern.match('121212ssss978787787value'))

pattern = re.compile(r'colou?r')
print(pattern.search('colour'))

pattern = re.compile(r'\b\w{3}\b')
print(pattern.findall('One two red blue'))

#escape() function is used to escape special characters in a string, so they can be treated as literal characters in a regex pattern.

import re

print(re.escape('$5.00'))
print(re.escape('file(1).txt'))

print(re.escape('C++'))
print(re.escape('a.b.c'))

print(re.escape('[abc]'))
print(re.escape('hello*world'))

print(re.escape('price?'))
print(re.escape('data+science'))

print(re.escape('name|age'))
print(re.escape('^start$'))

print(re.escape('{1,3}'))
print(re.escape('(abc)'))

print(re.escape('\\path\\to\\file'))
print(re.escape('user@example.com'))
print(re.escape('100% sure'))

#group() function is used to retrieve the matched groups from a regex match object. It can take an optional argument to specify which group to retrieve, or it can be called without arguments to retrieve the entire match.

import re

m = re.search(r'(\d{3})-(\d{2})-(\d{4})', '123-45-6789')
print(m.group(0), m.group(1), m.group(2), m.group(3))

m = re.search(r'(\w+) (\w+)', 'Hello World')
print(m.group(0), m.group(1), m.group(2))

m = re.match(r'(abc)(\d+)', 'abc123')
print(m.group(0), m.group(1), m.group(2))

m = re.search(r'(Hi|Hello) (\w+)', 'Hello John')
print(m.group(0), m.group(1), m.group(2))

m = re.search(r'(colou?r)', 'color')
print(m.group(0), m.group(1))

m = re.search(r'(start).*(end)', 'start middle end')
print(m.group(0), m.group(1), m.group(2))

m = re.search(r'(\d{2}):(\d{2})', '12:30 PM')
print(m.group(0), m.group(1), m.group(2))

m = re.search(r'([A-Z][a-z]+) ([A-Z][a-z]+)', 'John Doe')
print(m.group(0), m.group(1), m.group(2))

m = re.search(r'(\w+)@(\w+)\.(\w+)', 'test@gmail.com')
print(m.group(0), m.group(1), m.group(2), m.group(3))

m = re.search(r'(\d+)([a-zA-Z]+)', '123abc')
print(m.group(0), m.group(1), m.group(2))

# start(), end(), span() functions are used to retrieve the start and end positions of a match in the original string. They are


m = re.search(r'\d+', 'abc123xyz')
print(m.start(), m.end(), m.span())

m = re.search(r'world', 'Hello world')
print(m.start(), m.end(), m.span())

m = re.search(r'[A-Z]+', 'abcXYZdef')
print(m.start(), m.end(), m.span())

m = re.search(r'\bcat\b', 'A cat sleeps')
print(m.start(), m.end(), m.span())

m = re.search(r'end$', 'This is the end')
print(m.start(), m.end(), m.span())

m = re.search(r'\d{2}', 'Age 45 years')
print(m.start(), m.end(), m.span())

m = re.search(r'colou?r', 'colour is nice')
print(m.start(), m.end(), m.span())

m = re.search(r'[aeiou]', 'Python')
print(m.start(), m.end(), m.span())

m = re.search(r'\w{4}', 'Test code')
print(m.start(), m.end(), m.span())

m = re.search(r'[A-Z]{2,}', 'AB cd EFG')
print(m.start(), m.end(), m.span())