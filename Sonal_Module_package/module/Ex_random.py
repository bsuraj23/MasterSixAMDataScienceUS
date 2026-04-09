import random   
print(random.random())  #gives random float number between 0 and 1
print(random.randint(1,10))  #gives random integer between 1 and
print(random.randrange(1,10,2))  #gives random odd integer between 1 and 10
print(random.uniform(1,10))  #gives random float number between 1 and 10
print(random.choice(['apple','banana','cherry']))  #gives random element from the list