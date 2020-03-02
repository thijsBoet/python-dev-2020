import re

# REGEX rules
# -------------------------------------------------
# https://www.w3schools.com/python/python_regex.asp

string = 'search this inside this text please!'
print('search' in string)

# returns match object
matchObject = re.search('this', string)

# returns tuple of indeces
print(matchObject.span())
# returns start index
print(matchObject.start())
# returns end index
print(matchObject.end())
# returns first match
print(matchObject.group())

# can save pattern to variable
pattern = re.compile('this')

print(pattern.search(string))
# returns list of all matching patterns
print(pattern.findall(string))
# returns memory object if pattern is identical to entire string
# print(pattern.fullmatch(string))
# matches first characters while search scans foreward through the entire string
print(pattern.match(string))

# use https://regex101.com/ to create expressions
text = 'In the beginning God created the heaven and the earth. And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters. And God said, Let there be light: and there was light.'

pattern = re.compile(r'([a-zA-Z]).([a])')
matchObject = pattern.search(text)
print(matchObject.group())

pattern = re.compile(r'(God).([a-zA-Z]*)')
print(pattern.findall(text))
