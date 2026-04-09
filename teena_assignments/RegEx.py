import re   #built in package used to work with regular xpressions.

#Finding a specific pattern
#Checking if a document contains a specific keyword or pattern

log_entry = "ERROR 2026-03-13: Database connection failed."
# Look for 'ERROR' anywhere in the line
if re.search(r"ERROR", log_entry):
    print("Alert: Critical issue found in logs!")

# Validating input at the start

username = "user_99_beta"
# Check if the username starts with a letter and is followed by word characters
if re.match(r"[a-zA-Z]\w+", username):
    print("Valid username format.")
else:
    print("Invalid: Usernames must start with a letter.")

#Extracting Multiple Data Points

text = "Items cost $25.00, $45.50, and $10.00."
# Find all dollar amounts (digits followed by a decimal and two more digits)
prices = re.findall(r"\$\d+\.\d{2}", text)

print(prices)  # Output: ['$25.00', '$45.50', '$10.00']

#Cleaning or Reformatting Data

raw_data = "My phone number is 555-0123. Call me!"
# Replace all digits with an 'X' to hide the number
clean_data = re.sub(r"\d", "X", raw_data)

print(clean_data)  # Output: "My phone number is XXX-XXXX. Call me!"

