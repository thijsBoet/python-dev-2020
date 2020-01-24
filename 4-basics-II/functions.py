# Function should do ONE thing really well
# Should return something

def sum(num1, num2):
  return num1 + num2

print(sum(4, 5))

def say_hello(name='Darth vader', emoji='🦹‍♂️'):  # paramenters
    print(f'Hello {name}{emoji}')

say_hello()                                   # falls back to default paramenters when no argument is given

# positional arguments => position of name and emoji matter
say_hello('Matthijs', '😊')                   # arguments

# keyword arguments
say_hello(emoji='😊', name='Allen')  # bad code less readable / predictable

# age = input('What is yout age?: ')

def checkDriverAge(age = 0):
  if int(age) < 18:
	  print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
	  print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
	  print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge()

# Methods vs Functions
list()
print()

# Methods use a dot . and are owned by a object or datatype
greet = 'hi'.upper()
print('bye'.join(greet))

# Docstrings
def test(a):
  '''
  Info: this function test and prints param a
  '''
  print(a)

test('!!!')
# print(test.__doc__)

def is_even(num):
  return num % 2 == 0

print(is_even(2))

# *args => pass a variable number of arguments to a function
def myFun(*argv):
    for arg in argv:
        print (arg)

print(myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks'))

#  **kwargs => keyword arguments
def keywordFunc(**kwargs):
  print(kwargs)
  total = 0
  for items in kwargs.values():
    total += items
  return total

print(keywordFunc(num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs
def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

print(highest_even([50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Scope           => what variables do I have access to?
# Global scope    => access to variable in entire program bad practice
# Function scope  => only access in function scope

# interperter searches for variable
# 1 start with local scope?
# 2 parent local scope? | up a level
# 3 Global scope?
# 4 build in python functions

total = 0

def count():
  global total                      # access global variable bad practice
  total += 1
  return total

count()
count()
print(count())

# depenendy injection good practice to access global variable
total = 0

def count(total):
  total += 1
  return total

print(count(count(count(total))))  # nest function otherwise will return 1

# nonlocal => refers to parent local => usually bad practice
def outer():
  x = "local"
  def inner():
    nonlocal x          # use parent scope for x => "local"
    x = "nonlocal"      # redefine parent x as "nonlocal"
    print("inner:", x)

  inner()
  print("outer:", x)    # redefined outer scope with nonlocal keyword

outer()

# Global scope performance heavy
# Function scope more performant due to better garbage collection