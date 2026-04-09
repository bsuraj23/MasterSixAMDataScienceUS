#ex1
import math


try:
    file=open("C:\\AI_python\\AI path\\prompt.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File not found, please check the file path and name.")

#ex2
# try:
#     import mathe
#     print(math.sqrt(8))
# except ModuleNotFoundError:
#     print("Module not found")

#ex3
try:
    a = int(input("Enter a number: "))
    c = 10 + a
    print(c)
    raise RuntimeError("Manually raised error")
    
except ValueError:                    # ✅ Catches "abc" input
    print("Please enter a valid number!")
except RuntimeError as e:             # ✅ Catches manual raise
    print("Caught error:", e)


    

