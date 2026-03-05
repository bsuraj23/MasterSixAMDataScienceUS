#Immutable: int, float, str, tuple, frozenset, range etc.
N = 14
print(f'ID of N is {id(N)}')
N += 1
print(f'ID of N is {id(N)}')
print(f'Data type of N is {type(N)}')
print(f'N value is {N}')
print("")

N = 14.23
print(f'ID of N is {id(N)}')
N += 1.5
print(f'ID of N is {id(N)}')
print(f'Data type of N is {type(N)}')
print(f'N value is {N}')
print("")

S = "Hello"
#S[0] = h      --this will give error
print(type(S))
print("")

t = (1, 2, 3)
print(type(t))
# t[0] = 10     # --this will give error
print("")

F_set = frozenset([1, 2, 3, 4])
print(type(F_set))
print("")

r = range(0,5)
print(list(r))
print(type(r))
print(id(r))
r = range(1, 10, 2)
print(id(r))
print("")

#Mutable: list, dict, set, bytearray, etc.
#none is also a Datatype 
L = [1, 2, 3, 4, 5]         
print(type(L))
print("")

matrix = [[1, 2, 3], [4, 5, 6]]  
print(type(matrix))
print("")

data_set = {1, 2, 3, 4}                 
print(type(data_set))
print("")

dictionary = {"name": "Alice", "age": 30}           
print(type(dictionary)) 
print("")
         
x = None #none data type
print(type(x))
print(x)
print("")

# A key difference between bytes and strings is that bytes are immutable and don't support most string methods directly. 
# For example, you cannot concatenate a bytes object with a string without explicit conversion
b = b"Hello"
print(type(b))
print(b)
print(b.decode("utf-8"))  # Convert bytes to string
print(type(b.decode("utf-8")))
print("")

#bytearray
ba = bytearray([65, 66, 67])
print(type(ba))
print(ba)
print(ba.decode("utf-8"))
print(type(ba.decode("utf-8")))
print("")

#memoryview
mv = memoryview(b"Hello")
print(type(mv))
print(mv)
print(mv.tobytes())
print(mv.tobytes().decode("utf-8"))
print(type(mv.tobytes().decode("utf-8")))