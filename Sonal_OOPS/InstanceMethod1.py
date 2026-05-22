#Example 1
class cal():
    x=10
    def add(self,a,b):
        self.a=a
        self.b=b
        return a+b
obj=cal()
print(f"Sum is = {obj.add(10,40)}")
print(obj.a) #10
#print(cal.add(5,6)) #instance method can not called with class name

#Example 2
print("------------------------------------------------")
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def scale(self, factor):
        self.width *= factor
        self.height *= factor
        return f"Scaled by {factor}x"

rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")      # 15
print(f"Perimeter: {rect.perimeter()}")  # 16
print(rect.scale(2))               # width=10, height=6 now
