# creates __pycache__ everytime module is imported
import utility
# a package is a folder containing modules
# use . syntax to go down a directory to load modules from a package
import shopping.shopping_cart
# or to access functions directly use from package.module import functioname

from shopping.shopping_cart import buy
from utility import multiply, divide
# use * syntax to import every function
from utility import *

# prints the filepath
print(utility)
# use . syntax to run methods
print(utility.divide(10,5))
print(multiply(2,5))
# use . syntax to go down a directory to run methods
print(shopping.shopping_cart.buy('apple'))
print(buy('banana'))

# imported files return their name when they contain print(__name__)
# when the statement is not imported, but run directly from the file it will return "__main__"

# wont run because buy method was imported from shopping cart and not the main module
if __name__ == "__main__":
    buy('strawberry pi')

def add(num1, num2):
    return num1 + num2

# will run because add method was not imported, but run from main file
if __name__ == "__main__":
    print(add(5,5))

class Student():
    pass

st1 = Student()
# again returns __main__ because class was not imported, but run from main file
print(type(st1))

