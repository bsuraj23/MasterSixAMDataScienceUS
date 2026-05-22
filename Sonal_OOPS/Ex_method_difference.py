# class method and and static method both can called by class name directly,
class MyClass:
    a1 = 90  # Class variable
    def instance_method(self): ## Instance Method
        return f"Instance method called on {self}"
    # Class Method
    @classmethod 
    def class_method(cls):
        return f"Class method called on {cls}"
    # Static Method
    @staticmethod
    def static_method():
        return "Static method called"   
# Create an instance of MyClass
sam = MyClass() 
print(sam.instance_method())  # Instance method called on sam
print(MyClass.class_method())  # Calls class method
print(sam.class_method())
print(MyClass.static_method())  # Calls static method  

#Ex1
class Car:
    def __init__(self, color):
        self.color = color  # This car’s color

    #this is instance method because it is using instance variable self.color
    def describe(self):
        return f"This car is {self.color}"
    #getter 
    def get_color(self):
        return self.color   
    #setter 
    def set_color(self, new_color):
        self.color = new_color
        return f"Car color changed to {self.color}"
maruthi800 = Car("RED")
print(maruthi800.describe())  # "This car is RED
maruthi800.set_color("blue")  # Change color to blue
print(maruthi800.describe())  #"This car is blue
print(maruthi800.get_color())  # Get the current color using the getter
maruthi800.set_color("green")  # Change color to green
print(maruthi800.describe())  # Now maruthi800 is green!
my_car = Car("CYan")
print(my_car.describe())  # This car is CYan

#Ex2
class Circle:
    pi = 3.14159  # Class variable

    def __init__(self, radius):
        self.radius = radius  # Instance variable

    # Instance method
    def area(self):
        return Circle.pi * (self.radius ** 2)
    #getter
    def get_radius(self):
        return self.radius
    #setter
    def set_radius(self, new_radius):
        self.radius = new_radius
        Circle.pi = new_radius  # Just for demonstration, not typical usage
circle = Circle(5)
print(circle.area())  # Area of the circle with radius 5
print(circle.get_radius())  # Get the radius using the getter
circle.set_radius(10)  # Set a new radius using the setter
print(circle.area())  # Area of the circle with radius 10








