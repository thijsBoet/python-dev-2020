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