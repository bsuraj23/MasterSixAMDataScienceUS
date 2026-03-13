#function with no arguments
def my_function(): 
    print("This is my first function")
my_function()

#To find the square of a number
def square(num):
    return num * num
print(square(5))

#function with one argument Temperature Conversion used in weather app
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(celsius_to_fahrenheit(35))

#Calculate Discount - Shopping website
def apply_discount(price):
    final_price = price * 0.9 # applyimg 10% discount
    return final_price
print(apply_discount(1000))

#Check Even Number - Data validation
def is_even(number):
    if number % 2 == 0:
        return "Even number"
    else:
        return "Odd number"
    
print(is_even(11))

#Calculate Factorial
def factorial(n):
    result = 1 # because factorial multiplication starts with one
    for i in range(1, n+1): # Loop through numbers until n 
        result = result * i # Multiply the numbers
    return result
print(factorial(7))

# Factorial can also be written in recursion

#Function to count vowels in string
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for letter in text.lower():
        if letter in vowels:
            count += 1
    return count
print(count_vowels("python is very popular "))

#Function to check if number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))

#Function to check if number is prime for bigger numbers
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
      print(i) 
      if n % i == 0:
            return False
    return True
print(is_prime(61))

#Function to sum all numbers in list
def sum_List(num):
    total = 0 
    for n in num:
        total += n
    return total
print(sum_List([4,8,3,6]))

 #Function to find the length of a list
def list_length(items):
    count = 0
    for i in items:
        count += 1
    return count
print(list_length([10,8,4,3]))

#Email Validation - Used in sign up forms
def validate_email(email):
    if "@" in email and "." in email:
        return "valid email"
    else:
        return "Invalid email"
print(validate_email("john@gmail.com"))

#Calculate Tax - Used in Billing Systems
def calculate_tax(amount):
    tax = amount * 0.8
    return tax
print(calculate_tax(2500))

#Password Strength Checker(Security Systems) - Used in login or authentication systems
def check_password(password):
    if len(password) >= 8:
       return "strong Password"
    else:
       return "weak password"
print(check_password("welcome123"))

#File Size checker (DevOps or Cloud Systems)
def check_file_size(size):
    if size > 100:
        return "File too Large"
    else:
        return "File accepted"
print(check_file_size(560))

#Order Status Notification
def order_status(order_id):
    print("Checking the status for order:", order_id)

order_status(783665)

