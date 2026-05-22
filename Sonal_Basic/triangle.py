rows = 10


#Will print left triangle
for i in range(rows):
    print("*" * i )


#will print right trangle
# for i in range(rows):      
#     print(' ' * (rows-i) + '*' * i)

#will print equilateral triangle
for i in range(1, rows):    
    print(' ' * (rows - i) + '*' * (2 * i - 1))
    


    