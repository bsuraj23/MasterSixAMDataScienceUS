def add_numbers(a,b):
   h=a*b
   print(h)
   return a+b 
add_numbers(3,4) #Output: 12

def even_odd(n):
  if n%2==0:
    print("even")
  else:
    print("odd")
even_odd(5) #Output: odd
even_odd(10) #Output: even

def chr(str):
  count=0
  for chr in str:
    count=count+1
  print(count)
chr("hi") #Output: 2
 
def rev(str):
  h=""
  for chr in str:
    h=chr+h
  print(h)

rev("HELLO") #Output: OLLEH

def greet(name="likitha"):
  print("hello",name)

greet()


def sum_all(*args):
   return sum(args)

sum_all(1,3,4,5) #Output: 13

def details(**kwargs):
  print(kwargs)

details(name="Likitha", role="Data Engineer", city="Dallas")
#Output: {'name': 'Likitha', 'role': 'Data Engineer', 'city': 'Dallas'}

def fact(n):
  if n==1:
    return 1
  else:
    n=n*fact(n-1)
    return n

fact(5) #Output: 120

data = [("A",5),("B",2),("C",8)]
print(sorted(data, key=lambda x: x[1],reverse=True)) #Output: [('C', 8), ('A', 5), ('B', 2)]

def simple_interest(p, t, r=5):
   SI = (p * r * t) / 100
   return SI
simple_interest(1000,2) #Output: 100.0
simple_interest(1000,2,10) #Output: 200.0

sunil=10
def f1():
 sunil=15
 print("value of sunil inside f1",sunil)

f1()
print("value of sunil outside f1",sunil)

#Output:
#value of sunil inside f1 15
#value of sunil outside f1 10

#map function example
numbers = [1,2,3,4]
res=map(lambda x:x*x,numbers)
print(res)

def triangle(n):
    for i in range(1, n+1):
        print('ivalue',i)
        for j in range(i):
            print('jvalue',j)
            print("*", end="")
        print()
triangle(2)

#closure example
def power(n):
  def square(x):
    return x**n
  return square

square=power(2)

square(2)
#Output: 4


def converter(scale):

    def convert(celsius):

        if scale == "F":
            return celsius * 9/5 + 32

        elif scale == "K":
            return celsius + 273

    return convert

temp=converter("F")
temp(66)
#Output: 150.8

#genertor example
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for number in count_up_to(5):
    print(number)
#Output:
#1
#2      
#3
#4

#decorator example
def log(func):

    def wrapper(*args, **kwargs):

        print(f"Function {func.__name__} called with arguments {args}")

        result = func(*args, **kwargs)

        print(f"Function returned {result}")

        return result

    return wrapper

@log
def add(a, b):
    return a + b


print(add(2,3))
#Output:
#Function add called with arguments (2, 3)
#Function returned 5
#5  
