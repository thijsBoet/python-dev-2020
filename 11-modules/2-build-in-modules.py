# all build in modules
# https://docs.python.org/3/py-modindex.html

import random, sys

# returns filelocation of module
print(random)

# returns help documentation 
# --------------------------
# help(random)
# --------------------------

# retruns all the method names
print(dir(random))

# returns random number between 0 and 1
print(random.random())

# returns random integer between two integers
print(random.randint(1,10))

# picks random number from list
print(random.choice([1,2,3,4,5]))

# shuffles list
my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)

# returns current file path
print(sys.argv)

# returns current file path plus first argument
print(sys.argv[1])