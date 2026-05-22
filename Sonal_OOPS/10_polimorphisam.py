#Example of operator overloading.It is giving special meaning to operators (+, -, *, etc.) 
# Done using special method like __add__, __sub__, __mul__
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

n1 = Number(10)
n2 = Number(20)
print(n1 + n2)

#Function overloading is same function name with different parameters.Python 
#does NOT support it directly but we can simulate with default arguments *args

def add(*args):
    return sum(args)

print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5))
