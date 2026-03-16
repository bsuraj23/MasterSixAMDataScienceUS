#EX1
def add():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number"))
        print("Addition is ", a / b)   
    
    except ValueError:
        print("Invalid input, please enter numeric values.")
    except ZeroDivisionError:
        print("Division by zero error")
add()

# #Ex2   
# def add():
#     try:
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))
#         print("div is ", a / b)    
    
#     except Exception as e:  # Exception 'e'will Catches ALL exceptions
#              print("Error Details:",e)
# add()

