#Class Methods in Python
#A class method is a method that is bound to the class and not the instance of the class.
# It can modify a class state that applies across all instances of the class.   

class Car:
    manufacturer = "Toyota"  # This is a class variable (shared by all)

    @classmethod
    def set_manufacturer(cls, new_name):
        # We use 'cls' to modify the class variable directly
        cls.manufacturer = new_name

# Create two car instances
car1 = Car()
car2 = Car()

print(f"Before: {car1.manufacturer} and {car2.manufacturer}")