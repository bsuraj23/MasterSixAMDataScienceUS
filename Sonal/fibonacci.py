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
