try:
    lst = [1, 2, 3]                 
    print(lst[1]) 
    dict={"name":"sonal"}
    print(dict["age"])  # KeyError: 'age' not found in dict
except IndexError:
    print("Index out of range")
except KeyError: 
    print("Key not found which your trying to access")
finally:
    print("Execution completed.I am finally block")  