#Hierarchical inheritance is a type of inheritance where one base class is
#  inherited by multiple derived (child) classes.
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

class Bird(Animal):
    def speak(self):
        print("Bird chirps")
print(Bird.mro())
# Each subclass inherits from the same base class Animal
dog = Dog()
cat = Cat()
bird = Bird()

dog.speak()  # Dog barks
cat.speak()  # Cat meows
bird.speak() # Bird chirps