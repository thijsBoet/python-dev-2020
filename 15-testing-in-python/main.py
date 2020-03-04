# pylint
# auto Pep 8
# => unittest

def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'please enter number'
    except ValueError as err:
        return err

from random import randint

def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print(f'you are a genius!\n{guess} is the right number.')
            return
    else:
        print('only numbers between 1 and 10.')

if __name__ == '__main__':
    answer = randint(1,10)
    while True:
        try:
            guess = int(input('guess a number 1~10: '))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('please enter a number.')
            continue