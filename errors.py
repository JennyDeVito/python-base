#!/usr/bin/env python3

"""Script to explore the exceptions treatment"""

import os
import sys

#EAFP - Easy to Ask for Forgiveness than Permission
#tries to do someting, if it is not possible, do the exception
try:
    names = open("names.txt").readlines() #FileNotFoundError
#bare except: one exception for all errors - makes impossible to know what
#went wrong
#the right thing to do is to create an exception for every possible error
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    #TODO: use retry
#it is possible to use else in a try, but only if the except is false
else:
    print("Success!!!")
#the try has a finally argument - it is excecuted always, no matter what
finally:
    print("Always excecute this!")
    
#EAFP - Easy to Ask for Forgiveness than Permission
#tries to do someting, if it is not possible, do the exception
try:
    print(names[2])
except:
    print("[Error] Missing name in file")
    sys.exit(1)
