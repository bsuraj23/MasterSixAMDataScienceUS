#generator expression example
squares = (x*x for x in range(16))
print(next(squares)) 
print(next(squares))
print(next(squares))
print(squares)  
print(type(squares)) 

# def fibonacci():
#     a, b = 1, 2        # Start with first two numbers
#     while True:        # Infinite loop
#         yield a        # Give current number, pause here
#         a, b = b, a + b # Next: a=old b, b=sum (magic swap!)
#         # sum=a+b  #these 3 line of code does same like magic swap
#         # a=b
#         # b=sum
# # Get first 10 Fibonacci numbers
# fib = fibonacci()
# for _ in range(10):
#     print(next(fib)) # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
