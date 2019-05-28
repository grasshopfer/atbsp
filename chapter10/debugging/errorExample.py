#! python3

# when errors occur, python throws us a traceback. It throws, we just gotta catch it.

import traceback

def spam():
    bacon()

def bacon():
    raise Exception('This is an error message')

try:
    spam()
except:
    print('An error occurred. This is the traceback:\n' + traceback.format_exc())


print('If we get here, the program completed normally because the error was caught.')
