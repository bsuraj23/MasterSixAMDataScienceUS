str1 = "apple"
str2 = "banana"
def manual_compare(s1, s2):
# Calculate lengths manually
    len1 = 0
    for c in s1:
        len1 += 1
    len2 = 0
    for c in s2:
        len2 += 1
# Compare lengths and content manually
    if len1 != len2:
        return False
    for i in range(len1):
        if s1[i] != s2[i]:
            return False
    return True
print(manual_compare(str1, str2))  # False (different strings)