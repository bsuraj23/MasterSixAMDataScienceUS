# 1. Sujit's Original Example that prints a, b times
def repeat_line(a="Ram", b=1):
    for i in range(b):
        print(a)

repeat_line()           # Uses defaults
repeat_line("Hi", 2)    # Overrides the defaults with "Hi" and 2
#___________________________________________________________________

#2. The Order Rule: In Python, you cannot have a default argument before a non-default one.
#gives you error, due to fail of order
def repeat_line(a= 2, b):
    for i in range(b):
        print(a)

repeat_line() # will get error
repeat_line(3) # will get error
repeat_line(3,4) # will get error

#Otherway around is acceptable
def repeat_line(a, b = 1):
    for i in range(b):
        print(a)

repeat_line(3)
repeat_line(2,3)
# #___________________________________________________________________

#3. Mixed Arguments
#Rule: Non-default arguments MUST come before default arguments.
def greet(name, msg="Good morning"):
    print(f"Hello {name}, {msg}")

greet("Vijaya")                 # overrides the first argument
greet("Vijaya", "How are you?") # overrides the defaults
