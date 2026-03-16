def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


if __name__ == "__main__": 
    print("calling directly from my_math_module = ",__name__)   
    n = int(input("Enter first number: "))
    m = int(input("Enter second number: "))
    print("Addition: ", add(n, m))
    print("Subtraction: ", subtract(n, m))
    print("Multiplication: ", multiply(n, m))
else:
    print("calling from Ex_module.py = ",__name__)
    n = int(input("Enter first number: "))
    m = int(input("Enter second number: "))
    print("Addition: ", add(n, m))
    print("Subtraction: ", subtract(n, m))
    print("Multiplication: ", multiply(n, m))
 

    

