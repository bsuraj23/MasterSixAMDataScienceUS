# Example 1
# x = 100
# print("first line ", locals()) #that prints the current local namespace dictionary

# # Example 2
# y = "Python"
# print("y found in globals:", 'y' in globals())



# Example 4
# z = [1, 2, 3]
# print("Globals keys:", list(globals().keys()))


# Example 5
#print(globals().keys())
#need to create global()(global namespace dictionary) when Variable names come from runtime data (files, APIs, user input)
#Inside functions needing to create new globals dynamically
def modify_global():
     globals()['new_var'] = "Created Globally"

modify_global()
print(new_var)
