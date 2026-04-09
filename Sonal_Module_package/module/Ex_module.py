import my_math_module as mm
import os
import sys
#from my_math_module import subtract

#without main block in my_math_module.py  o/p my_math_module
#print("Ex_module---",subtract(300,100))

print("filename--",mm.__file__)# Output: Path to the module file
print("module--",mm.__name__)      # Output: my_math_module
print("package--",mm.__package__)   # Output: None (since it's a top-level module)
print("loader--",mm.__loader__)    # Output: <_frozen_importlib_external.SourceFileLoader object at ...>
print("spec--",mm.__spec__)      # Output: ModuleSpec(name='my_math_module', loader=<_frozen_importlib_external.SourceFileLoader object at ...>, origin='...')       


print("Current working directory is: ", os.getcwd())  # Output: Path to current directory
print("Python version is: ", sys.version)  # Output: Python version






