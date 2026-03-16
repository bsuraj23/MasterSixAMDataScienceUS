#ex1
try:
    [1, 2, 3][10]
except IndexError:
    print("IndexError occurred")

#ex2
try:
    {}["key"]
except KeyError:
    print("KeyError occurred")

#ex3
try:
    print(undefined_variable)
except NameError:
    print("NameError occurred")
