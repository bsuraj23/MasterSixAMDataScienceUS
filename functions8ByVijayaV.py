#Classic example of Python, Generating Fibonacci series for user desired number
def fibonacci(n):
  sequence = []
  a,b = 0, 1
  while len(sequence) < n:
    sequence.append(a)
    a,b = b, a+b
  return sequence
print(fibonacci(10))

# #using generator:
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))

# using lamda and reduce:
from functools import reduce
def fibonacci(n):
    return reduce(lambda x, _: x+[x[-2]+x[-1]], range(n-2), [0,1])[:n]

print(fibonacci(10))
