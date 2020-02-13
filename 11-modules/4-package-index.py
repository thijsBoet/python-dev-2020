# https://pypi.org/
# pip install package

import pyjokes

print(pyjokes.get_joke('en', 'neutral'))

# always create environments using pipenv to keep modules contained to projects
# https://pypi.org/project/pipenv/

# pipenv --python 3.7

# usefull modules
from collections import Counter, defaultdict, OrderedDict

li = [1,1,1,2,3,4,4,4,5,6,7]
sentence = 'The quick brown fox jumps over the lazy dog'
# creates a dictionary that counts the occurances of the keyvalues
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda: 'non existing value => dictionary["c"]', {'a': 1, 'b': 2})
# returns the first function/object when a non existing value is called
print(dictionary['c'])

# OrderedDict depricated as dictionaries as of Python 3.7 are ordered by default
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2
# checks if the order of insertion is the same
print(d == d2)

d3 = OrderedDict()
d3['b'] = 2
d3['a'] = 1
print(d2 == d3)

import datetime, time, array

print(datetime.date.today())

# arrays are more performant than lists
# list parameter is type code like 'i' for int and second is the list/array
arr = array('i', [1,2,3])