
def count_up_to(n): 
    count = 1
    while count <= n:
        yield count
        count += 1 
        
# counter = count_up_to(5)
# for number in counter:
#     print(number) 

counter = count_up_to(5)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3  

# def infinite_counter():
#     count = 1
#     while True:
#         yield count
#         count += 1
# inf_counter = infinite_counter()
# for _ in range(5):
#     print(next(inf_counter))


    


