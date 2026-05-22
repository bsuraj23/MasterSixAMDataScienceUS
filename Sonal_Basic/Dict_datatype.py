#dictionary datatype which is mutable

# My_dict={"kashvi":8,"vedang":15,"niva":11}
# print(My_dict["kashvi"])  #output=8
# print(My_dict.get("vedang"))  #output=15
# My_dict["sonal"]=45 #adding new key pair value in dictionary
# print(*My_dict.keys())  #output=dict_keys(['kashvi', 'vedang', 'niva']))


d1 = {} 
#or
d2 = dict()

# d3 = {'name1': 'ajay', 'name2': 'vijay', 'Name3': 'sampton'}
# #or
# d33=dict(name1='ajay', name2='vijay', Name3='sampton')

# d4 = dict(zip(['a', 'b'], [1, 2]))

# d5 = {x: x**2 for x in range(5)} # d5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

d = {'a': 1, 'b': 2}

d=dict([('a', 1), ('b', 2)]) #with dict() constructor

#print(*d.keys())
# print(*d.values())
# print(*d.items())

#It overwrites the value if the key already exists.
# d.update({'c': 3}) #It adds new key-value pairs if the key does not exist.
# print(d)
a=d.pop('b') #indict pop() methos need to be pass one key and it will remove that key and return the value of that key
print(a) #will print value of b which opped out
# a=d.pop('b')
# print(a)


#nested dictionary
d2 = {'a': {'x': 1}, 'b': {'y': 2}}
#print(*d2.keys())
for k, v in d2.items():
     print(k+"="+str(v))
#print(*[f"{k}:{v}" for k, v in d2.items()])


d5 = {'Name': {'class': {'Ms Valsuk': 12}},
        'Sonal': {'class': {'Ms Henry':11}}}

#k means key is in string and value is another dictonary which needs to convert in string
for k, v in d5.items():
    print(k+"="+str(v))


#dictonary with list values
d = {'fruits': ['apple', 'banana']}
d2 = {'marks': [85, 90, 95]}
d3 = {'letters': list('abc')}
d4 = {'nums': list(range(5))}
d5 = {'data': [1.1, 2.2, 3.3]}
# print(d)
# print(d2)
# print(d3)
print(d4)
print(d5.values())

for k, v in d4.items():
    print(k+"="+str(v))
     



