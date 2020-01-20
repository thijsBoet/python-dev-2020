is_old = False
is_licenced = True

if is_old and is_licenced: # no parenthesis or curly brackets just colon and indentation
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
print('' == 1)              # will convert different values to the same type bool('') == bool(1)
print([] == 1)
print(10 == 10.0)
print([] == [])

print(True is 1)            # is checks equality of both type and value
print('' is 1)              # will not convert different values to the same type
print([] is [])             # still false because both lists live in differnt memory spaces
print((1,2,3) is (1,2,3))   # same goes for tuples and dictionaries
print([1,2,3] is [1,2,3])