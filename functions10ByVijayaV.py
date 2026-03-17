#Function that gives out any text in reverse order
def reverse_string(text):
  reverseString = "" #python creates a new string to hold the reverse string
  for newchar in text:
    reverseString = newchar + reverseString #imp line: our logic
  return reverseString

print(reverse_string("hello"))

# more concise way using slicing
def reverse(text):
  return text[::-1]
print(reverse("hello"))