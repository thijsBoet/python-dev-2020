# Use try except blocks to raise errors and not halt program excecution

try:
  with open('test.txt', mode='r') as my_file:
    print(my_file.read())
except FileNotFoundError as err:
  raise err
except IOError as err:
  raise err