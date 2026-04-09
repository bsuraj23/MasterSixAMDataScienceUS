#Menu System Using Function Aliasing
def start():
    print("Starting the system...")

def stop():
    print("Stopping the system...")

def restart():
    print("Restarting the system...")

# Aliases
s = start
x = stop
r = restart

menu = {
    "1": s,
    "2": x,
    "3": r
}

choice = input("Enter 1=start, 2=stop, 3=restart: ")

if choice in menu:
    menu[choice]()
else:
    print("Invalid choice")
