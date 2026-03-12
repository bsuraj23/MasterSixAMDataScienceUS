#A geneartor produces a value one at a time instead of returning all at once

#yield - pauses the function
#next - resumes the fumnction

def sample_gen():
    yield 1
    print("Hi I am inside the generator")
    yield 2
    print("Hi..Yielded 2")
    yield 3
    print("Hi..Yilded 3")

gen=sample_gen()
print(next(gen))
print(next(gen))
print(next(gen))

def sample_gen1(n):
    for i in range(1,n+1):
      yield i

g=sample_gen1(5)
for inum in g:
    print(inum)

#generator without using yield

gen=(x*x for x in range(5))
gen1=(x+1 for x in range(3))

for i in gen:
    print("looping thru gen ")
    print(i)

for i in gen1:
    print(i)

#generators are great for large data but can b run only once

#send() - send value to the generator and resume execution
# same like next() but passes data to the generator

def multiplier():
    while True:
        num=yield
        print("Received =",num*2)

g=multiplier()

next(g)
print("Callimg function:",g.send(5))
g.send(10)