# # #Calculator: perfect example for conditional branching and input validation
def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

print(calculator(10, 5, 'add'))
print(calculator(10, 0, 'divide'))
print(calculator(10, 9, 'ADD'))
#print(calculator(10, 'blah', 'divide')) #will get error as we are not handeling non numerical inputs for a and b

#-------------------------------------------------------------------------------------------------------

def calculator(a,b, operation):
  operation = operation.lower() #normalizing the data
  if isinstance(a, (int, float)) & isinstance(b, (int, float)): #sanitizing the data/Type checking 
    #using dictionary for mapping instead of long if else statements
    actionToDo = {"add": a+b,
                  "subtract": a-b,
                  "multiply": a*b,
                  "divide": a/b if b != 0 else "can't devide by 0"}
    return actionToDo.get(operation, "not valid operation")
  else:
    return "Error: Please provide numbers only"

print(calculator(21,3, "multiply"))
print(calculator(21,0, "DIVIDE"))
print(calculator(21,"hi", "DIVIDE"))



