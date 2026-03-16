def is_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("madam")) 


list =[1, 2, 3, 4, 5]
print(list[0:3])
list = list * 2
print(list)