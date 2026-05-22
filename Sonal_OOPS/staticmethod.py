# Static methods can be called on the class itself without creating an instance.
# They are often used for utility functions that don't need access to instance or class data.
# Static methods do not modify class or instance state.
# They are just grouped within the class for organizational purposes.
#Example of static method in Car class
class Car:  
    def __init__(self, color):
        self.color = color  # This car’s color

    # Static method to describe the car
    @staticmethod
    def describe(): #staticmethod doesn't take nay argument
        return "This is a car."
my_car = Car("red")
print(my_car.color)  # red  
print(Car.describe())  # Call static method using class name
print(my_car.describe())  # Call static method using instance (not common but possible)
#Both ways of calling static method are valid, but using the class name is more common.

#rarely used methods in real world scenarios. 