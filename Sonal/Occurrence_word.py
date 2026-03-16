def word_frequency(text):
    words = text.lower().split() #split() never returns anything but a list
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

sentence = "Python is fun and python is easy"
print(word_frequency(sentence))



#variable length args
def multiply(*args): # accept any number of positional arguments
    result = 1
    for num in args:
        result *= num
        #result = result * num
    return result   
print(multiply(1, 2, 3))        # Output: 6
#print(multiply(4, 5))           # Output: 20








