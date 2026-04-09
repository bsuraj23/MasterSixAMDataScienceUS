# Generator is a function that returns values one at a time using Yield instead of returning everything at once. 

#examples on generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)

# more example
def count_numbers(n):
    for i in range(1, n+1):
        yield i

for num in count_numbers(5):
    print(num) 

# more example - using generator to produce even numbers
def numbers():
    for i in range(1,100):
        if i%2==0:
           yield i

for n in numbers():
    print(n)

#generator example - to produce squares of numbers
def squares():
    for i in range(1,6):
        yield i*i
for n in squares():
    print(n)
#without yield
def squares():
 squares= (i*i for i in range(1,6))
for n in squares:
    print(n)    
squares()