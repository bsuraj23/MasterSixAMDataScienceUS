# Assertions
#Example:1
# age  = 9
# assert age >= 18, "age should be greater than 18 for voter id msg here "


# Example:2 List not empty
marks = [3]
assert len(marks) > 0, "Marks list cannot be empty"  

#Example:3
def divide(a, b):
    assert b != 0, "Division by zero!"
    return a / b
print(divide(10, 3))

#Example:4
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        assert self.balance >= amount, f"Insufficient funds: {self.balance}"
obj=BankAccount(8000)
obj.withdraw(8000)

#Example:5 # Types of assert Statements
x = 10
assert x == 10  #simple assert
assert x > 11, "x must be positive" #assert with message

