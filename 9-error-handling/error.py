li = [0,1,2,3]
di = {'a':1}

#                               Common Errors
# ----------------------------------------------------------------------------

# TypeError: must be str, not int
# sum('1', 2)

# SyntaxError: invalid syntax
# def hooo()
#    pass

# NameError: name 'name' is not defined
# 1 + name        

# IndexError: list index out of range
# li[4]

# KeyError: 'b' key does not exist
# di['b']

# ZeroDivisionError: division by zero
# 5/0

#                               ErrorHandling
# ----------------------------------------------------------------------------

# Use try/except block for exceptions
# Use while loop to keep running program after exception
while True:
    try:
        # set input as int type so it must be a number | no empty string or letter
        age = int(input('What is your age? '))
        print(f'Your age is {age}.')
    # You can define the type of error the exception handles
    except ValueError:
        print('Please enter a number.')
    # You can define the type of error the exception handles
    except ZeroDivisionError:
        print('Please enter age higher than 0.')
    else:
        print('Thank you!')
        break

def sum(num1, num2):
    # Can build try/except block direct into function
    try:
        return num1 + num2
    # Good practice to define the type of error for debugging purposes
    except TypeError as err:
    # use 'as err' to catch error variable message
        print('Please enter numbers. ' + err)


sum('1', 2)