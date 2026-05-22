#Example of try-except-else-finally
try:
    print("Try")
except:
    print("Except")
else:
    print("Else")
finally:
    print("Finally")

#Example of  Control Flow in nested try-except-finally
print("------------")
try:
    try:
        print("Inner try")
        x = 1 / 0
    except ZeroDivisionError:
        print("Inner except")
    finally:
        print("Inner finally")
except:
    print("Outer except")
finally:
    print("Outer finally")

#Example of Control Flow in try-except
print("------------")
try:
    print("Try block")
    x = 1 / 0   #immediately raises a exception so "After error"never prints.
    print("After error")
except ZeroDivisionError:
    print("Except block")
print("After try-except")

#Control Flow in try-except-finally
print("------------")

try:
    print("Try")
    x = 1 / 0
except ZeroDivisionError:
    print("Except")
finally:
    print("Finally")
print("After all")