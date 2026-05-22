# class Parent:
#     def __init__(self):
#         print("Parent constructor")

# class Child(Parent):
#     def __init__(self):
#         super().__init__() #super method must declare in first line of child method
#         print("Child constructor")
#        # Call the parent class constructor

# obj = Child()
print("-"*35)
#Another example
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

    def info(self):
        print("This is an animal.")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()           # Call parent method first
        print("Dog barks: Woof!")      # Then add child behavior
            
class Cat(Dog):
    def make_sound(self):
        super().make_sound()           # Reuse parent behavior
        print("Cat meows: Meow!")
   
# Create objects and test
d = Dog()
d.make_sound()
c = Cat()
c.make_sound()

