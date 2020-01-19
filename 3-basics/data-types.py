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

alpha = ['x', 'a', 'b', 'c', 'd', 'e', '3','!', '1', '&']

print(alpha.index('a'))             # returns the index of given value
print(alpha.index('c', 0, 5))       # look between index 0 and 5
print('a'in alpha)                  # returns True if value is in alpha
print('i' in 'hi my name is thijs') # also works on strings
print(alpha.count('d'))             # counts accurances of set value
alpha.sort()                        # sorts excisting array/list
print(alpha)
print(sorted(alpha))                # creates a new copy and sorts it
alpha.reverse()                     # reverses but does not sort
print(alpha)   
print(alpha[::-1])                  # reverses with list slicing
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

tuple


set
dict

# Classes -> custom types

# Specialized Data Types -> Modules