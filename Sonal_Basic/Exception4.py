try:
    num = k
except:
    print("Error occurred")  #A bare except: catches ALL exceptions in Python
else:
    print("No exception, num is", num)
finally:
    print("Execution completed")