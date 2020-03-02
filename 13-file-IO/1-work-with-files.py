# IO == input/output
# like input image => output compressed image
from os import chdir

chdir('D:\\python\\python-dev-2020\\13-file-IO\\')

my_file = open('test.txt')

print(my_file.read())
print(my_file.readline())

# sets cursor back to beginning of file, otherwise starts reading from ending of file
my_file.seek(0)
print(my_file.readlines())

# removes file as reference object from memory
my_file.close()