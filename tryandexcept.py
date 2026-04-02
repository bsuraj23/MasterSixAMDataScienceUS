try:
    print("Try block")
    x = 1/1
    a = [12,3,34,45]
    print(a[4])  # This will raise an IndexError
    print("After error") #this line will not be executed
except ZeroDivisionError:
    print("Caught division by zero error")
except IndexError:
    print("Caught index error")

print("After try-except block")


# Another example of handling IndexError
try:
    arr = [10, 20, 30]
    print(arr[5])   # ❌ IndexError
except IndexError:
    print("Index out of range!")


#Another example of handling ZeroDivisionError through user input
try:
    arr = [1, 2, 3, 4]
    index = int(input("Enter index: "))
    print(arr[index])
except IndexError:
    print("Invalid index! Please enter a valid position.")
except ValueError:
    print("Please enter a number.")    
          