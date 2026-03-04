def is_present(text, word):
    if word in text:
        return True
    else:
        return False
text = "The quick brown fox jumps over the lazy dog"
word = "fox"
print(is_present(text, word))  # True (word is present in the text)
word = "cat"
print(is_present(text, word))  # False (word is not present in the text) 

#same code with out using in operator

def is_present(text, word):
    # Calculate lengths manually (avoiding len() if you want total manual control)
    text_len = 0
    for char in text:
        text_len += 1
    word_len = 0
    for char in word:
        word_len += 1
    # An empty word is technically present at the start of any string
    if word_len == 0:
       return True
    # Loop through the main text
    # We only need to go up to (text_len - word_len)
    for i in range(text_len - word_len + 1):
        match = True
    # Check if the substring starting at index 'i' matches 'word'
        for j in range(word_len):
            if text[i + j] != word[j]:
               match = False
               break
    # If the inner loop finished without finding a mismatch
    if match == True:
       return True
    return False
# Testing the code
main_string = "hello world"
search_word = "world"
if is_present(main_string, search_word):
    print(f"'{search_word}' was found!")
else:
    print(f"'{search_word}' was not found.")
