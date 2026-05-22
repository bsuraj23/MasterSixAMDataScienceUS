# Single except Block that can handle Multiple Exceptions

values = [
    "abc",     # string with invalid value → ValueError
    ["20"]]     # list (wrong type) → TypeError
for x in values:
    
    try:
        age = int(x)    # can raise ValueError or TypeError depending on x
        if age < 0:
            pass
    except (ValueError, TypeError) as obj:
        if isinstance(obj, ValueError):
            print(f"value error occured for - {x}")
        else:
            print(f"Type error occured for - {x}")
    
        
