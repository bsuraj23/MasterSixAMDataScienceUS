classroom = {
    "student_01": {
        "name": "Leo",
        "grade": "A",
        "subjects": ["Math", "Science"]
    },
    "student_02": {
        "name": "Maya",
        "grade": "B",
        "subjects": ["History", "Art"]
    }
}

# Accessing Maya's grade
print(classroom["student_02"]["grade"])  # Output: B

# Accessing Leo's first subject
print(classroom["student_01"]["subjects"][0])  # Output: Math

#Adding or Updating Nested Data
# Changing Leo's grade
classroom["student_01"]["grade"] = "A+"
print(classroom["student_01"]["grade"])  # Output: A+
