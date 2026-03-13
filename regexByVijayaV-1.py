
import re
#re.match() only checks from the beginning of the string. If the pattern is not found at the start, it returns None.
#\d → any digit (0–9) and + → one or more times
# r in r'\d+' means raw string


#Digits:


print('1. ', re.match(r'\d', '1abc')) # string start with sigle digit, yes
print('2. ', re.match(r'\d+', '1234abc')) #string start with digits, yes
print('3. ', re.match(r'\d', '1234abc')) #string start with digit,then yes and only gets the starting position, not the position for 1234
print('4. ', re.match(r'\d+', 'a2bc')) #doesn't start with a digit or digits, so NO
print('5. ', re.match(r'\d+', 'abc')) #doesn't start with a digit or digits, so NO
print('6. ', re.match(r'\d+', 'abc2')) #doesn't start with a digit or digits, so NO

# match and ^ is technically redundant, because match already checks from the start, but it often used for clarity and protability
print('7. ', re.match(r'^\d', '5days')) # string matches a single digit at the beginning
print('8. ', re.match(r'^\d', '56days')) # string matches a single digit at the beginning, so it only brings the position of that first digit, not the position of 56

print('9. ', re.match(r'\d{2}', '45672abc')) #string starts with atleast 2 digits, it returns a matching object showing the position of those 2 digits
print('10. ', re.match(r'\d{3}', '45abc')) # string starts with atleast 3 digits, NO
print('11. ', re.match(r'\d{2,4}', '45672abc')) #string starts with a specific range of digits, here for ex: 2 to 4 digits, so since it has max 4, it will bring the position of 4 nums

#any Charecter: 
print('12. ', re.match(r'.+','')) #none, because of empty string
print('13. ', re.match(r'.+','ramramramramram')) #starts with any one or more charecter except newline, YES, gets you the position of ramramramramram

# Words or charecters:
# \w is equivalent to: [A-Za-z0-9_]


print('14. ', re.match(r'\w+', 'Hello123')) #string starts with word or words, yes
print('15. ', re.match(r'\w+', 'Hello 123 hi')) #string starts with word so yes
print('16. ', re.match(r'\w+', '123Hello')) #string starts with word, Yes
print('17. ', re.match(r'\w+', '123')) #string starts with word, yes, because w+ is letters,digits and underscore
print('18. ', re.match(r'\w+', '')) # doesn't start with words, NO
print('19. ', re.match(r'\w+', '_123')) # yes because of string starting with underscore
print('20. ', re.match(r'[A-Z]', 'Python3ajshjdsgasgdasudfgdhsss')) #string starts with only upper case, Yes
print('21. ', re.match(r'\w+', '@123')) #@ is not a letter,digit or underscore, so NO
print('22. ', re.match(r'[A-Za-z]+', '123')) # is NO as we are specifing if the string starts with letters

#match vs fullmatch: 

# re.match(): Checks only at the beginning of the string. The rest of the string does not have to match
# re.fullmatch(): The entire string must match the pattern. Nothing extra is allowed before or after

print('23. ', re.match(r'\bis\b', "is this going to work")) #string starts with is, So YES
print('24', re.fullmatch(r'\bis\b', "is this going to work")) #string does not only contain is, so NO
print('25. ', re.search(r'\bis\b', "is this going to work")) #searches if string has is, so Yes


print('26. ', re.match(r'\bis\b', "This is good")) #string doesn't start with is, So NO
print('27. ', re.fullmatch(r'\bis\b', "This is good")) #string contains other than is, So NO
print('28. ', re.search(r'\bis\b', "This is good")) # string contains the word is, SO YES


#Search

#re.search() looks through the entire string and returns the first match it finds. If nothing matches, it returns None.
# r in r'\d+' means raw string

print('29. ', re.search(r'\d+', 'abcxyz')) #serches the entire string for one or more digits, NO
print('30. ', re.search(r'\d+', 'abc4xyz')) #you get the position of the digit 4, YES
print('31. ', re.search(r'\d+', 'ab4cxy2z')) #only gets the position of first digit in the string, returns the position of 4
print('32. ', re.search(r'is', 'The black cat is here.')) #searches for the word is and returns its position, again, it gets first instance only
print('33. ', re.search(r'is', 'This island is beautiful')) #***IMP***It will match "is" inside "This", not the word is.
print('34. ', re.search(r'\bis\b', 'This island is beautiful')) # To match the whole word, you have to use, \b is \b, this will get you the actual word is
print('35. ', re.search(r'[a-z]+', 'helloWorldTest')) # it matches the lower case word, so gets you hello
print('36. ', re.search(r'table$', 'This is the table')) # $ searches the string if it ends with table
print('37. ', re.search(r'5$', 'This is the table 5')) # string that ends with digit 5, YES
print('38. ', re.search(r'^\w+', '12 Start123 end')) # ^ → start of string, \w → word characters (letters, digits, underscore),+ → one or more
print('39. ', re.search(r'^\w{5,10}', '12Star6 end')) # string starts with 5 to 10 charecters, very useful for validating usernames

#optional charecters
print('40. ', re.search(r'colou?r', 'The color is nice')) # here u is optional, can appear 0 or 1 time, so gets you color

# detecting whitespace (tab, newline, space)
print('41. ', re.search(r'\s', 'vyvy   here')) #gets you the first space 
print('42. ', re.search(r'\s+', 'hi    Ram')) #regex looks for a sequence of spaces because of \s+

