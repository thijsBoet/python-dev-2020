li = [0,1,2]
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
        10/age
    # You can define the type of error the exception handles
    except ValueError:
        print('Please enter a number.')
        # continue continues back to top of loop
        continue
    # You can define the type of error the exception handles
    except ZeroDivisionError:
        print('Please enter age higher than 0.')
        break
    else:
        print('Thank you!')
        # break will stop excution
        break
    # finally runs after everything has executed even after break statement
    finally:
        print('ok, i am finally done.')

def sum(num1, num2):
    # Can build try/except block direct into function
    try:
        return num1 + num2
    # Good practice to define the type of error for debugging purposes
    except (TypeError, ZeroDivisionError) as err:
    # use 'as err' to catch error variable message
        print(err) 

sum('1', 2)