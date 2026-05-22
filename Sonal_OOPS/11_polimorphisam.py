#Polymorphism allows objects of different types to be treated through a 
# common interface, with each type providing its own behavior

class Dog:
    def speak(self):
        print("Dog says: Woof!")

class Cat:
    def speak(self):
        print("Cat says: Meow!")

# Polymorphism in action
def animal_sound(animal):
    animal.speak()  # same method name, different behavior

d = Dog()
c = Cat()

animal_sound(d)  # Dog says: Woof!
animal_sound(c)  # Cat says: Meow