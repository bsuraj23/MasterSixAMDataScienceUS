# A decorator is something that adds extra behavior to a function without changing the function itself.

#Example - A Company app has a page to view employee salaries
# First check if user is logged in or not. if user is logged in then only allowd to see the salaries page.
def my_decorator(func):
    def wraffer():
        print("Checking if user is loggedin or not")
        func()
        return wraffer()
@my_decorator
def view_salaries()
    print("Showing salary detailsof employees")

        