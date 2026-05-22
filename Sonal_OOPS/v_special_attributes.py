#special attributes (also known as magic attributes, dunder attributes, or
#  double-underscore attributes

#Ex:1 of __eq__ and __ne__
print("---"*25)
class Item:
    def __init__(self, product_id):
        self.product_id = product_id
            
    def __eq__(self, other): #item1.__eq__(item2)
        return self.product_id == other.product_id

    def __ne__(self, other):
        return self.product_id != other.product_id

# Usage
item1 = Item("laptop")
item2 = Item("laptop")  # Same product
print(item1 == item2)  # True (same product)
print(item1 != item2)  # True (different products)

#without __eq__ , pythone by default compares memory address

#Ex:2 __delattr__ : delete attribute of an object"
print("---"*25)
class Person:
    def __init__(self):
        self.name = "Alice"

    def __delattr__(self, name):
        print(f"Deleting {name}")
        super().__delattr__(name)#whithout this Python never removes the attribute;
        #it just runs your print and stops. The attribute still exists.

p = Person()
del p.name
#print(p.name)
#if attribute doesn't exist, will raise AttributeError




