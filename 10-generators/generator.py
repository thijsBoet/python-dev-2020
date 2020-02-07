# generators can generate a sequence of values in a memory effecient way by creating an object
# range is a generator and creates an object with sequencetial values
range(1000)
# list creates a giant list by iterating over a value in memory one by one.
list(range(1000))

# generators are not kept in memory like the iterable make_list function
def make_list(num):
  result = []
  for i in range(num):
    result.append(i * 2)
  return result

print(make_list(10))

# generators use the keyword yield for iteration
# yield pauses the function and creates an object with sequencetial values
def generator_function(num):
  for i in range(num):
    # instead of return we use yield
    yield i*2

# really fast due to generator
for item in generator_function(10000):
  print(item)

# creates a generator object
g = generator_function(10000)
print(g)

# next creates next iteration of generator_function
# next only keeps track of the last value of i in memory (mem effecient)
print(next(g))  # 0 * 2 = 0
print(next(g))  # 1 * 2 = 2
print(next(g))  # 2 * 2 = 4

# test effeciency between generator object and iterable list object
from time import time
import math

def performance(func):
    def wrapper_func(*args, **kwargs):
        beginTime = time()
        result = func(*args, **kwargs)
        endTime = time()
        print(f'{func} took {round((endTime - beginTime), 5)} seconds to complete.')
        return result
    return wrapper_func

@performance
def long_time():
    print('1')
    for i in range(100000):
        i * 5

@performance
def long_time2():
    print('2')
    for i in list(range(100000)):
        i * 5

# twice as fast
long_time()
# takes about twice as long
long_time2()

# how for loops work under the hood
def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      print(iterator)
      print(next(iterator))
    except StopIteration:
      print('StopIteration exception')
      break

special_for([1, 2, 3])

# create own generator from scratch
class MyGen():
  current = 0
  def __init__(self, first, last):
    self.first = first
    self.last = last

  def __iter__(self):
    return self

  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration

# fibonacci sequence with generator
gen = MyGen(0, 10)
for i in gen:
  print(i)

def fib(num):
  a = 0
  b = 1
  for i in range(num):
    yield a
    temp = a
    a = b
    b = temp + b

for x in fib(20):
  print(x)

# fibonacci sequence with list
def fib2(num):
  a = 0
  b = 1
  result = []
  for i in range(num):
    result.append(a)
    temp = a
    a = b
    b = temp + b
  return result

print(fib2(10))