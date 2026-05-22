#delete static variable
class Student:
    school = "ABC School"
print(Student.school)
del Student.school
#print(Student.school)  #will through an error

#modify static variable
# class Student:
#     school = "ABC School"
#     def change_school(self, new_name):
#         Student.school = new_name
# s1 = Student()
# s2 = Student()  
# print(Student.school)  # Accessing static variable via class
# s1.change_school("MET")  # Modifying static variable via instance method     
# print(Student.school)  # Accessing static variable via class    
# print(s2.school)

