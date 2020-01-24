is_old = False
is_licenced = True

if is_old and is_licenced:  # no parenthesis or curly brackets just colon and indentation
    print('You are old enough and are licenced to drive!')
elif is_licenced:
    print('You are licensed, but not yet old enough to drive!')
else:
    print('You are not old enough to drive!')
# Truthy and Falsy

# python interprets values to Truthy or Falsy
old = 'Hello'   # == bool('Hello')  => True aka Truthy
licensed = 0    # == bool(0)        => False ake Falsy

password = '123'
username = 'johnny'

if password and username:
    print("password and username exist.")

# Ternary operator
is_friend = True
can_message = "Message allowed" if is_friend else "Not allowed to message"
print(can_message)

# Short Ciruiting
is_Friend = True
is_User = True

if is_Friend or is_User:          # Short circuiting when skipping a 2nd condition
    print('Best friends forever')

# Logical Operators
print(4 > 5)
print(4 < 5)
print(4 == 5)
print(1 < 2 < 3 < 4)
print(1 >= 0)
print(1 >= 0)
print(0 != 0)
print(not True)
print(not False)
# and | or | not

is_magician = False
is_expert = True

if is_magician and is_expert:
    print("You are a master magician.")
elif is_magician and not is_expert:
    print("At least you are getting there.")
elif not is_magician:
    print("You need magic powers.")

print(True == 1)            # == checks equality of value
# will convert different values to the same type bool('') == bool(1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

print(True is 1)            # is checks equality of both type and value
print('' is 1)              # will not convert different values to the same type
# still false because both lists live in differnt memory spaces
print([] is [])
print((1, 2, 3) is (1, 2, 3))   # same goes for tuples and dictionaries
print([1, 2, 3] is [1, 2, 3])

# Loops
for item in 'Zero to Mastery':
    print(item)

for item in [1, 2, 3, 4, 5]:    # iterate over a collection of items
    print(item)

print(item)                     # prints last iteration 5

for item in [1, 2, 3, 4, 5]:    # nested loop
    for x in ['a', 'b', 'c']:
        print(item, x)

# iterable can be a list, dictionary, tuple, set, even strings
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user.items():
    key, value = item             # tuple unpakking
    print(key, value)

for key, value in user.items():   # short hand tuple unpakking
    print(key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# counter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0

for num in my_list:
    counter += num

print(counter)

# range object creates list from 0 (if none given) to 2nd parameter -1 (99)
print(range(100))
print(range(0, 10, 2))        # start, stop, stepover

for _ in range(0, 10):        # use underscore for unnamed variables
    print(_)

for _ in range(10, 0, -1):    # -1 stepover value for backward range
    print(_)

print(list(range(10)))        # creates list range from 0 to 9

for i, char in enumerate('Hello'):
    # enumerate gives both the value and the index of a iterable object
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'Index of 50 is: {i}')

i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('\'break\' out while loop.\nWill not run after break statement in while loop.')

# while loop more flexable with initialisation of variable and control over itteration | use for unknow amount of itterations
# for loop more predictable | use for known amount of itterations

while True:                   # True is always True
    # input('say Hello ')
    break                     # break out of infinite loop

# break     => exit loop
# continue  => continue back to top of loop statement
# pass      => does nothing => placeholder for future code

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
    for pixel in row:
        if pixel:
            print('*', end="")
        if pixel == 0:
            print(' ', end="")
    print('')

# good code is:

# clean
# readable
# predictable
# DRY     =>  dont repeat yourself
# KISS    =>  keep it simple stupid

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

