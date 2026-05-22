class Car:
    def __init__(self, brand, year):  # Constructor
        self.brand = brand
        self.year = year
        print(f"Constructor: {brand} created")

    def __del__(self):  # Destructor
        print(f"Destructor: {self.brand} destroyed")

    def display(self):
        print(f"Car: {self.brand} ({self.year})")

# Usage
my_car = Car("Toyota", 2023)  # Calls constructor
my_car.display()
del my_car  # Triggers destructor (timing may vary)
#my_car.display()  once delete the object, it will through an error
