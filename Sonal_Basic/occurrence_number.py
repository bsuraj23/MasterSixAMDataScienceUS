def number_frequency(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1    # ← get(num, 0) with INTEGER key
    return freq


user_numbers = input("Enter numbers (space separated): ").split()
numbers = [int(x) for x in user_numbers]  # Convert strings to integers

result = number_frequency(numbers)
print("Number frequencies:")
for num, count in result.items():
    print(f"{num}: {count}")
