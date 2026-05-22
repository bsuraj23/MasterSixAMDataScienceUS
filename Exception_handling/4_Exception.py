# try with Multiple except Blocks
# try:
#     y=int(input("Enter any value: "))
#     x = 100/y
# except ZeroDivisionError:
#     print("Zero is not allowed")
# except ValueError:
#     print("ValueError")


# Nested try-except-finally Blocks
print("------------")
try:
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("Inner except")
finally:
    print("Outer finally")

# How to Print Exception Information
print("---------")
try:
    x = 1/0
except Exception as e: 
    print("Exception info:",e)

print("---------------")
try:
    x = int(["20"])
except Exception as e: 
    print("Exception info:",e)



