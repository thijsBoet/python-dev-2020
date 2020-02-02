#! pyhon3

def hello(func):
    print('helllllooooo')

greet = hello
del hello

# still works because only hello was deleted not greet
# print(greet())

# Higher order Function:

# 1 ) functions that accept other functions as arguments (map, filter, reduce, zip etc)
def greet1(func):
    func()

# 2 ) functions that return another function
def greet2():
    def func():
        return 5
    return func

# DECORATORS super charge our functions 
def my_decorator(func):
    def wrap_func():            # We can alter functionality in this wrapper
        print('************')   # Like adding stars
        func()
        print('************')
    return wrap_func            # => not calling it => ()

@my_decorator
def hello2():
    print('helllllooooo')

hello2()

# Under the hood works like this
a = my_decorator(hello2)
a()

@my_decorator
def bye():
    print('byebyebyebye') 
    
bye()

# DECORATOR with possible multiple parameter and keyword parameters
# AKA Decorator pattern
def my_2nd_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func

@my_2nd_decorator
def hello3(greeting, emoji):
    print(greeting, emoji)

hello3('hiiii', ';)')

# Performance Decorator
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
    for i in range(100000):
        i*5

long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)