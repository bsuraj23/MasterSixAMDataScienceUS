#Static method = normal function inside a class
#Ex1
class Employee:
    def __init__(self, name, title):
        self.name = name
        self.title = title

    @staticmethod
    def is_valid_title(title):
        # A utility to check if a title is in our allowed list
        allowed_titles = ["Manager", "Developer", "Designer", "HR"]
        return title in allowed_titles #returns Boolean value

# You don't need an Employee object to use this!
Role=Employee.is_valid_title("Developer")
if Role:
    print("This is a valid title.")
else:
    print("Invalid title.")

#Ex2
print("-----------------------------------------------")
class User:
    @staticmethod
    def is_valid_email(email):
        return '@' in email and '.' in email

print(User.is_valid_email("test@example.com"))  # True
  



    
