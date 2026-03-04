def count_repeats(text):
    unique_chars = []
    counts = []
    # 1. Iterate through the string to build frequency lists
    for char in text:
        found_index = -1
        for i in range(len(unique_chars)):
            if unique_chars[i] == char:
                found_index = i
                break
        if found_index == -1:
            unique_chars.append(char)
            counts.append(1)
        else:
            counts[found_index] += 1
    # 2. Print characters that repeat
    print("Repeated characters and their counts:")
    for i in range(len(unique_chars)):
        if counts[i] > 1:
            print(f"'{unique_chars[i]}': {counts[i]} times")
# Example usage
input_string = "hello world"
count_repeats(input_string)     