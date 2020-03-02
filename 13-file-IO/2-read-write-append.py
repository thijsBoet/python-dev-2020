from os import chdir

chdir('D:\\python\\python-dev-2020\\13-file-IO\\')

# using "with" no need for .close() or seek(0) for cursor methods
with open('test.txt', mode='r') as my_file:
    print(my_file.readlines())

# non default write mode for writing to file overwrites text, because cursor is set to 0
with open('test.txt', mode='w') as my_file:
    pass

# use r+ to read and write
with open('test.txt', mode='r+') as my_file:
    text = my_file.write('hey it\'s me!')
    print(text)

# use a append mode to append to end of file and don't overwite text
with open('test.txt', mode='a') as my_file:
    text = my_file.write(':-)')

# write mode creates file if it does not yet exist
with open('sad.py', mode='w') as my_file:
    text = my_file.write(':-(')