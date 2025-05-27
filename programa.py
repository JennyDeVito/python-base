"""CLI arguments input test

Separates the CLI arguments inputted by the user

Execution

    python3 programa.py --arg1=arg --arg2=arg --arg3=arg ...

"""
__version__ = "0.1.0"
__author__ = "Jenny DeVito"
__license__ = "Unlicense"

#module to import
import sys

#create a dict
arguments = {}

#basic iteration, starts in 1 because we don't want the program's name
#in the list
for arg in sys.argv[1:]:
    key, value = arg.split("=")
    arguments[key.lstrip('-').strip()] = value.strip()

#print dict
print(arguments)
