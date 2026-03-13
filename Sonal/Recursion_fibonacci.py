def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
        Print(fibonacci(n-1) + fibonacci(n-2))
print(fibonacci(7))  #0,1,1,2,3,5,8 sum of last two digits 5+8 =13
