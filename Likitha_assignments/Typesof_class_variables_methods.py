#Global variable
country = "India"


# Function outside class
def course_info():
    print("This is a Python OOP practice program.")


class Student:
    # Class variable (shared by all objects)
    school = "ABC School"

    def __init__(self, name, marks):
        # Instance variables (different for each object)
        self.name = name
        self.marks = marks

    # Instance method
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("School:", self.school)
        print("Country:", country)

    # Instance method
    def add_bonus(self, bonus):
        self.marks = self.marks + bonus

    # Class method
    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

    # Static method
    @staticmethod
    def is_pass(marks):
        return marks >= 35


# Calling function outside class
course_info()

#Creating Objects
s1 = Student("Likitha", 80)
s2 = Student("sai", 30)

print("Before Bonus")
s1.display()
print()
s2.display()

print("Add Bonus to One Student")
s2.add_bonus(10)

print(" After Bonus")
s1.display()
print()
s2.display()

print(" Static Method Check")
print("Likitha pass?", Student.is_pass(s1.marks))
print("sai pass?", Student.is_pass(s2.marks))

print("Change Class Variable Using Class Method")
Student.change_school("XYZ School")

print(" After Changing School")
s1.display()
print()
s2.display()

print(" Direct Access to Class Variable ")
print(Student.school)