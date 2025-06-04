#!/usr/bin/env python3

"""Script to explore the exceptions treatment"""

import os
import sys

#LBYL - Look Before You Leap
#look for the file before trying to open it
#fif exists, ok, if it doesn't personalizes the error message so the user
#doesn't have access to the scripts (or the programs) sensitive's information
if os.path.exists("names.txt"):
    print("O arquivo exitste")
    input("...") #simulation of a race condition
    names = open("names.txt").readlines()
else:
    print("[Error] Missing file names.txt")
    sys.exit(1)

#LBYL - Look Before You Leap
#checks the lenght of the names list before trying to print it
#fif exists, ok, if it doesn't personalizes the error message so the user
#doesn't have access to the scripts (or the programs) sensitive's information
if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in file")
    sys.exit(1)
