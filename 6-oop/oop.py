# OOP paradime a way to structure our code in way that is easier to maintain, extend and write.

# 4 pillars of OOP

# Encapsulation binding the code and data into a single unit.
# Abstraction hiding unwanted details while showing most essential information.
# Inheritance new objects inherit the properties of excisting objects
# Polymorphism Poly = many | Morphism = forms => gives different outputs with same function see player_attack(char)

# Class aka blueprint
class PlayerCharacter:              # classes are capitalized, camelcased and singular
  membership = True                 # class object attribute => static attribute unlike dynamic attribute self.name
  def __init__(self, name='anon', age=0):
    # use underscores to signify private variables | may not be changed after initialization
    self._name = name               # property / attribute
    self._age = age

  def intro(self):                  # method
    print(f'Hi my name is {self._name} and im {self._age} years old.')

  @classmethod                      
  def adding_things(cls, num1, num2): # cls stands for class
    return cls('Teddy', num1 + num2)# instanciation of class object within method

  @staticmethod                     # same as classmethod, but no access to cls
  def adding_things2(cls, num1, num2):
    return num1 + num2

# everything in python is an object => class
# class is the blueprint for an object/instance
# objectsinstances are different instantiations of that class

# instanciations aka objects
player1 = PlayerCharacter('Cindy', 51)
player2 = PlayerCharacter('Tom', 47)
player2.attack = 50
player3 = PlayerCharacter.adding_things(2, 3)

print(player1.intro())
print(player2._name)
print(player2.intro)
print(player2.attack)
print(player3._age)

print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))
print(type(player1))

# inheritance of User class
class User():
  def sign_in(self):
    print('logged in')

class Wizard(User):       # inherit parent class (User)
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'attacking with power of {self.power}.')
    
class Archer(User):
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'attacking with arrows: arrows left {self.num_arrows}.')

wizard1 = Wizard('Gandalf', 50)
archer1 = Archer('Robin', 100)
archer1.sign_in()
wizard1.attack()
archer1.attack()

def player_attack(char):
  char.attack()

# different outputs with same function == PolyMorphism
player_attack(wizard1)
player_attack(archer1)

# different outputs with same function == PolyMorphism
for char in [wizard1, archer1]:
  char.attack()

# check if it is an instance of CLASSNAME
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))

object # base object class in Python aka everthing is an object in Python
print(isinstance(wizard1, object))

#Given the below class:
class Cat:
  species = 'mammal'
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def this(self):
    return self

# 1 Instantiate the Cat object with 3 cats
yoda = Cat('Yoda', 3)
simba = Cat('Simba', 2)
bubbles = Cat('Bubbles', 4)

# 2 Create a function that finds the oldest cat
def get_oldest_cat(*args):
	return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2:
print(f'The oldest cat is {get_oldest_cat(yoda.age, simba.age, bubbles.age)} years old.')
print(yoda.this())

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Yoda(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('Simon', 4), Sally('Sally', 21), Yoda('Yoda', 1)]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk()