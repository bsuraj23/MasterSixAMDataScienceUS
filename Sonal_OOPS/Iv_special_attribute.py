#Ex:1 annotations in this example provide type information 
# for documentation and tooling, but do not affect how the function runs
print("---"*25)
def add(a: int, b: int) -> float:
    return a + b
print(5+9)
print(add.__annotations__)
#__annotations__ is metadata for tools, not Python runtime

#Example:2 __annotations__
print("---"*25)
def multiply(x:int,y:float) -> int:
    print( x * y)
multiply(5,6.1)
print(multiply.__annotations__)

# Class annotations
print("---"*25)
class Car:
    color: str
    speed: int = 0
    
    def accelerate(self, increment: int) -> None:
        self.speed += increment

# Check all annotations
print("Function:", multiply.__annotations__)
print("Class:", Car.__annotations__)
print("Method:", Car.accelerate.__annotations__)






