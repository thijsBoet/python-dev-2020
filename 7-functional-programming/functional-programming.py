#! python3

# Functional programming is all about separation of concerns
# Each part concerns itself with the part it's really good at
# Unlike OOP where data and functionality is combined in properties and methods
# functional programming passes data through pure functions that do one thing really well
# But in the end the goals are the same as OOP and both ar not mutually exclusive

# 1   Clear & understandible
# 2   Extendable
# 3   Maintainable
# 4   Efficient
# 5   DRY

# Prime Pillar of Functional Programming is
# -------------- PURE FUNCTION ------------

# Pure function given same input will ALWAYS return same output
# Pure functions should NEVER produce any side-effects (does it interact with the outside world beyond the scope of the pure function)

# [1,2,3]   ->   Function   ->   [2,3,4]

def multiply_by2(li):
  new_list = []
  for item in li:
    new_list.append(item * 2)
  return new_list

print(multiply_by2([1, 2, 3]))

# previous OOP program in functional paradigm
wizard = {
  'name': 'Merlin',
  'power': 50
}

def attack(char):
  return f'{char["name"]} attacks with power of {char["power"]}.'

print(attack(wizard))

# COMMON FUNCTIONAL METHODS => map, filter, zip and reduce
# --------------------------------------------------------
my_list = [1,2,3]
your_list = [10, 20, 30]
their_list = [100, 200, 300]

# map(function, data)
def multiply_by_two(item):
  return item * 2

print(list(map(multiply_by_two, my_list)))

# filer(function, data)
def only_odd(item):
  return item % 2 != 0

print(list(filter(only_odd, my_list)))

# zip(first_list, second_list) like a zipper lists two lists together as tuples
print(list(zip(my_list, your_list)))

# reduce needs to be imported from functools
from functools import reduce

# reduce(function, sequence, initial item index)
# reduce list of values to ONE value
def accumulator(acc, item):
  print(acc, item)
  return acc + item

print(reduce(accumulator, my_list, 0))
print(reduce(accumulator, my_list, 10))

# lambda expressions => one time anonymous function
#              lambda param: function(param)
print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item , my_list))
print(list(map(lambda item: item ** 2, my_list)))

# sort tuples ascending with second value
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda x: x[1])
print(a)

from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
my_pets = map(lambda x: x.capitalize(), my_pets)
print(list(my_pets))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

print(list(filter(lambda score: score > 50, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
print(reduce(accumulator, (my_numbers + scores)))

# list, set, dictionary comprehentions
# slow old way
my_list = []

for char in 'Hello':
  my_list.append(char)

print(my_list)

# fast new way using list comprehensions

# my_list = [param for param in iterable]
new_list = [char for char in 'Good Bye']
print(new_list)

new_list2 = [num for num in range(0,100)]

# iterate with an expression over a list
new_list3 = [num * 2 for num in range(0,100)]

# filter for only even numbers
new_list4 = [num ** 2 for num in range(0,100) if num % 2 == 0]

# set comprehention, just use curly braces instead of brackets
my_set1 = {char for char in 'All set'}
print(my_set1)

my_set2 = {num for num in range(0,100)}

# dictionary comprehension, just use curly braces instead of brackets and key/value pairs as arguments
simple_dict = {
  'a' : 1,
  'b' : 2,
  'c' : 3,
  'd' : 4
}

my_dict = {key:value**2 for key,value in simple_dict.items() if value % 2 == 0}
print(my_dict)

my_dict2 = {num:num*2 for num in [1,2,3]}

# get duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([char for char in some_list if some_list.count(char) > 1]))
print(duplicates)