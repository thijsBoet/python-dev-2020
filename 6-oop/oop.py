# OOP paradime a way to structure our code in way that is easier to maintain, extend and write.

# Class aka blueprint
class PlayerCharacter:              # classes are capitalized, camelcased and singular
  def __init__(self, name, age):
    self.name = name                # properties
    self.age = age

  def run(self):                    # methods
    print('run')
    return 'done'

# everything in python is an object => class
# class is the blueprint for an object/instance
# objectsinstances are different instantiations of that class

# instanciations aka objects
player1 = PlayerCharacter('Cindy', 51)
player2 = PlayerCharacter('Tom', 47)
player2.attack = 50

print(player1.run())
print(player2.name)
print(player2.age)
print(player2.attack)

print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))
print(type(player1))