import translate

try:
  with open('beowulf.txt', mode='r') as my_file:
    text = my_file.read()
except FileNotFoundError as err:
  raise err
except IOError as err:
  raise err