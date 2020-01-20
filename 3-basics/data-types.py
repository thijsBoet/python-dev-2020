import math

# Fundamental Data Types
int
print(type(2 + 4))
print(type(2 - 4))

float
print(type(2 / 4))      # 0.5
print(type(8.9 + 1.1))  # 10.0

print(2 ** 3)
print(5 // 4)
print(6 % 4)

# math functions
print(round(3.1))
print(abs(-20))
print(math.ceil(3.1))
print(math.factorial(10))
print(math.pi)

# operator precedence

# ()
# **
# * /
# + -

print(bin(5))           # convert to binary value
print(int('0b101', 2))  # convert back to decimal value

str
print(type("Strings are texts"))
long_string = '''WOW
O O
---'''
print(long_string)
first_name = 'Matthijs'
last_name = 'Boet'
age = 38
full_name = first_name + ' ' + last_name
print(full_name)
print("It\'s \"kind of\" sunny.")                   # escape characters \'
print(f'Hi {full_name}. You are {age} years old.')  # formatted string f
print(full_name[0])                                 # index starts at 0
print(full_name[0:8])                               # 2nd is stop at index
print(full_name[0:14:2])                            # 3rd is step increased index
# full_name[start:stop:stepover]
print(full_name[::-1])                              # string reverse
print(len(full_name))                               # gives string length starts at 1
quote = 'To be or not to be.'
print(quote.upper())                                # uppercases
print(quote.find('be'))                             # returns index of first occurence or -1 for not found
print(quote.replace('be', 'me'))

bool
age_over_18 = True                                  # either True or False (Always Capitilized)
age_over_65 = False
print(bool(1))
print(bool(0))
print(bool('True'))
print(bool('False'))

# type conversion
print(type(int(str(100))))

# birth_year = input('What year were you born?\n')
# age = 2020 - int(birth_year)
# print(f'Your age is {age}.')

# username = input('What\'s your username?\n')
# password = input('Please enter your super secret password.\n')
# password_length = len(password)
# hidden_password = '*' * password_length

# print(f'{username}, your password {password_stars} is {len(password)} letters long.')

list
li = [1, True, "Hello", 2.5]                        # Like Arrays
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
print(amazon_cart[0])                               # indexed from 0
# amazon_cart[start:stop:stepover]
print(amazon_cart[1:3])
print(amazon_cart[1:4:2])
amazon_cart[0] = 'laptop'                           # Lists are mutable unlike Strings that are immutable
# Matrix multidimentional arrays/lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][0])
basket = [1,2,3,4,5]
print(len(basket))
basket.append(6)        # add value to end
print(basket)
basket.insert(0, 100)   # add value at index
print(basket)
basket.extend([100])    # appends object of same type code
print(basket)
basket.pop()            # pops last value
print(basket)
basket.pop(0)           # pops value at index code
print(basket)
basket.remove(6)        # remove value from list/array
print(basket)
basket.clear()          # clears list completely
print(basket)

alpha = ['x', 'a', 'b', 'c', 'd', 'e', '3','!', '1', '&', '&']

print(alpha.index('a'))             # returns the index of given value
print(alpha.index('c', 0, 5))       # look between index 0 and 5
print('a'in alpha)                  # returns True if value is in alpha
print('i' in 'hi my name is thijs') # also works on strings
print(alpha.count('d'))             # counts accurances of set value
alpha.sort()                        # sorts excisting array/list
print(alpha)
print(sorted(alpha))                # creates a new copy and sorts it
print(alpha)
print(alpha[::-1])                  # reverses with list slicing
alpha.reverse()                     # reverses but does not sort
print(list(range(1,100)))           # creates range list from 1 to 100
sentence = '<>'
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])
print(new_sentence)
# list unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)

None                                # absence of value just like NULL

dict                                # Dictionary unordered key => value pair(s) like associative array in PHP or objects JS
dictionary = {
    'a': [1,2,3],
    'b': 'Hello to all',
    'c': True
}
print(dictionary['a'])
print(dictionary['a'][1])
print(dictionary)

my_list = [
    {
        'a': [1,2,3],
        'b': 'Hello to all',
        'c': True
    },
    {
        'a': [4,5,6],
        'b': 'Bye to all',
        'c': False
    }
]
print(my_list[0]['a'][2])

vandale = {
    123: [1, 2, 3],
    '456': [4, 5, 6],
    '456': 'Bye',                   # Key must be unique, otherwise value is overwritten
    True: 'Hello',
    'is_magic': True,
}
print(vandale[True])                # Key must be immutable so no lists
print(vandale['456'])

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}
print(user.get('age'))              # get method returns None instead of 'Fatal Error' that halts excecution
print(user.get('age', 55))          # creates a default value of 55 when current value is None

user2 = dict(name='JohnJohn')       # other uncommon method of creating dictionaries
print(user2)

print('basket' in user)             # returns True or False if value excists
print('size' in user)
print('basket' in user.keys())      # just checks the keys, not the values
print('basket' in user.values())    # just checks the values, not the keys
print(('basket', [1, 2, 3]) in user.items())  # checks for tuples

user3 = user.copy()                 # copies dictionary
print(user.clear())                 # clears all dictionary values
print(user3)
print(user3.pop('age'))             # returns the value that was removed by pop method
print(user3.update({'age': 55}))    # updates age key/value to 55
user3.update({'code': '5'})         # even creates key/value pair if not yet excists
print(user3)

tuple                               # Like lists, but immutable
my_tuple = (1, 2, 3, 4, 5, 5, 5)    # less flexable than lists, but more performant
print(my_tuple[1])                  # can access individial values
print(5 in my_tuple)

new_tuple = my_tuple[1:4]           # can use slicing just like in lists
print(new_tuple)
x, y, z, *other, a = (1, 2, 3, 4, 5)
print(a)
print(other)
print(my_tuple.count(5))            # counts the occurrances of set value
print(my_tuple.index(5))            # returns index of given value
print(len(my_tuple))                # lenght

set                                 # unordered collection of unique values
my_set = {1, 2, 3, 4, 5, 5, 5, 5}
my_set.add(100)
my_set.add(2)
print(my_set)                       # only returns unique values so 2 and 5 are not added
print(set(alpha))                   # removes all duplicate values by converting it to a set
print(1 in my_set)
print(len(my_set))                  # only counts unique values
print(list(my_set))                 # still only returns unique values
new_set = my_set.copy()             # copy
my_set.clear()                      # clears all values
print(new_set)

old_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print(old_set.difference(your_set)) # returns unique values of old_set
old_set.discard(5)                  # discards specified value
print(old_set)
old_set.difference_update(your_set) # duplicate values are removed from old_set
print(old_set)
old_set.add(4)
old_set.add(5)
print(old_set.intersection(your_set)) # returns common values from both sets
print (old_set & your_set)          # short hand for intersection
print(old_set.isdisjoint(your_set)) # returns True for no common values, False for common duplicate values
print(old_set.union(your_set))      # unites both sets, but removes any duplicates
print(old_set | your_set)           # short hand for union method
print(old_set.issubset(your_set))   # True if all values from old_set fit in your_set
print(old_set.issuperset(your_set)) # True if all values from old_set encompass your_set

# Classes -> custom types

# Specialized Data Types -> Modules