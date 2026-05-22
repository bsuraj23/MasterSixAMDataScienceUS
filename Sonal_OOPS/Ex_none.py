x = None
print(x)  # None

# Check if None (use 'is', not '==')
if x is None:
    print("No value")  # This runs



def greet(name=None):
    name = name or "World"
    print(f"Hello {name}")
greet()        # Hello World
greet("Sonal") # Hello Sonal