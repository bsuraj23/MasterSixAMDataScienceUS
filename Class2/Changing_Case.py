# Using predifined functions
S = "Manhitha Dendi"
print(S.upper())   # MANHITHA DENDI
print(S.lower())   # manhitha dendi
print(S.title())   # Manhitha Dendi
print(S.swapcase())# mANHITHA dENDI


# Using user defined functions
LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def upper_case(input_string): #Converts a string to uppercase without built-in functions.
    result = ""
    for char in input_string:
        if char in LOWER_ALPHABET:
            index = 0         # Find the index of the lowercase character
            while index < len(LOWER_ALPHABET):
                if LOWER_ALPHABET[index] == char:
                    break
                index += 1
            result += UPPER_ALPHABET[index]  # Add the corresponding uppercase character
        else:
            result += char   # Keep non-alphabetic characters as they are
    return result

def lower_case(input_string):   # Converts a string to lowercase without built-in functions.
    result = ""
    for char in input_string:
        if char in UPPER_ALPHABET:
            index = 0  # Find the index of the uppercase character
            while index < len(UPPER_ALPHABET):
                if UPPER_ALPHABET[index] == char:
                    break
                index += 1
            result += LOWER_ALPHABET[index] # Add the corresponding lowercase characters
        else:
            result += char  # Keep non-alphabetic characters as they are
    return result

# Example usage
given_string = "HeLLo WorLD! 123"

uppercase_string = upper_case(given_string)
lowercase_string = lower_case(given_string)

print(f"Original string: {given_string}")
print(f"Uppercase: {uppercase_string}")
print(f"Lowercase: {lowercase_string}")