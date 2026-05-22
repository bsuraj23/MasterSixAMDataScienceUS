#The difference is Python's "small integer caching" optimization.
# lists Never cached (always new objects)


#ex1
a = [1, 2]
b = [1, 2]     # Same content, different objects
x=1000
y=1000
c = a             # Same object
print(id(a), id(b), id(c))      # Different, Different, Same
print(a is b)      # False - different objects
print(x is y)
# print(a is c)      # True  - because "is" checking for memory address
# print(a == b)      # True  because "==" checking for value

#Ex:2
# class Database:
#     def __init__(self):
#         self.connection = None  # No connection yet
    
#     def connect(self):
#         if self.connection is None:  # Check SAME object
#             print("Creating new connection...")
#             self.connection = "DB_CONNECTION_123"  # Simulate connection
#         else:
#             print("Reusing existing connection")
#         return self.connection
    
#     def query(self, sql):
#         if self.connection is None:
#             print("No connection! Connect first.")
#             return None
#         print(f"Executing: {sql} on {self.connection}")

# # Usage
# db1 = Database()
# db2 = Database()

# # First connection - creates new
# conn1 = db1.connect()      # "Creating new connection..."
# print(f"db1 conn: {id(conn1)}")

# # Same object reused ✓
# conn2 = db1.connect()  
# print(f"db2 conn: {id(conn2)}")    # "Reusing existing connection"
# print(f"is same? {conn1 is conn2}")  # True - SAME object!

# # Different instance = different connection
# conn3 = db2.connect()  # "Creating new connection..."
# print(f"db3 conn: {id(conn3)}")     
# print(f"db1 vs db2: {conn1 is conn3}")  # True - DIFFERENT objects
# #All are pointing to the same dbconnection so having same connection id and memory address as well
# # Query uses same connection
# db1.query("SELECT * FROM users")  # Works with existing connection


