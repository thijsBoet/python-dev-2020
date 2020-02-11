# from random import randint

# lowestNum = abs(int(input('What would you like to be the lowest number? ')))
# highestNum = abs(int(input('What would you like to be the highest number? ')))

# randomNumberRange = random.randint(lowestNum, highestNum)
# guessedNumber = abs(int(input(f'Guess a number between {lowestNum} and {highestNum}. ')))

# while guessedNumber != randomNumberRange:
#     print("Try and guess again!")
#     guessedNumber = abs(int(input(f'Guess a number between {lowestNum} and {highestNum}. ')))

# if guessedNumber == randomNumberRange:
#     print("You guessed right!")

from random import randint
answer = randint(1, 10)
# answer = randint(int(sys.argv[1]), int((sys.argv[2]))

while True:
    try:
        guess = int(input('guess a number 1~10: '))
        if guess > 0 and guess < 11:
            if guess == answer:
                print('You are a genius')
                break
    except ValueError:
        print('please enter a number between 1 and 10')
        continue