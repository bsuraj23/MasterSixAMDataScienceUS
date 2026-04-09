#Ex1:fibonacci without recursive
def fibonacci(n):
    """ This function returns the fibonacci series upto n terms """
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        #a, b = b, a + b  #Pythonic swap method
        temp = a + b      # ✅ Temp stores next value
        a = b             # ✅ Shift: a becomes old b
        b = temp 
    return series
print(fibonacci(6))


#Ex2: Fibonacci with recursive
# def fibonacci(n):
#         if n <= 1:
#             return n
#         return fibonacci(n-1) + fibonacci(n-2)
#         Print(fibonacci(n-1) + fibonacci(n-2))
# print(fibonacci(7))  #0,1,1,2,3,5,8 sum of last two digits 5+8 =13
