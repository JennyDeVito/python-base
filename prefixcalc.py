#!/usr/bin/env python3

"""Prefix calculator.

Function:

[operation] [n1] [n2]

Operations:
sum -> +
sub -> -
mul -> *
div -> /

Usage:
$ prefixcalc.py sum 5 2 --'logfilename'
The result is = 7

$ prefixcalc.py mul 10 5 --'logfilename'
The result is = 50

$ prefixcalc.py
operation: sum
n1: 5
n2: 4
Log filename: filename
The result is = 9

The results will be saved in filename.log
"""

__version__ = "0.1.3"
__author__ = "Jenny DeVito"
__license__ = "Unlicense"

import os
import sys
from datetime import datetime

#reads CLI arguments from the program name
arguments = sys.argv[1:]

#if there were none arguments asks the user to input
#Validation
if not arguments:
    operation = input("Operation: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    logfilename = input("Type your log's filename: ")
    arguments = [operation, n1, n2, logfilename]	
    
#checks if there are 4 arguments and kills program if there aren´t 
elif len(arguments) != 4:
    print("Error! Invalid number of arguments")
    print("Example: 'sum 7 6 --logfilename'")
#sys.exit(1) tells the terminal that the program ended in error
    sys.exit(1) 
#unpacks arguments into operation and numbers into a list nums
operation, *nums, logfile = arguments

#adjusts the log filename so it results in a proper filename with a .log in the end
logfile = logfile.lstrip("-") + ".log"

#create a list of valid operations
valid_operations = ("sum", "sub", "mul", "div")

#checks if the operation is valid if not show the valid operations
#and kills the program
if operation not in valid_operations:
    print("Invalid Operation")
    print(valid_operations)
    sys.exit(1)

#number validation
#create a empty list for validated numbers
validated_nums = []
#iterates on each number in nums
for num in nums:
    #TODO: usar while mais exeptions
    #checks if is a number
    if not num.replace(".","").isdigit():
        print(f"Invalid Number {num}")
        sys.exit(1)
    #if the number has a '.' turns it into a float
    if "." in num:
        num = float(num)
    #if not turns it into a integer
    else:
        num = int(num)
    #put the number into the validated number's list
    validated_nums.append(num)

#tries to unpack the validated numbers list into two variables: n1 and n2
try:
    n1, n2 = validated_nums
except ValueError as e:
    print(f"{str(e)}.")
    sys.exit(1)

#perform the operations
#TODO: usar dict de funcoes
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    if n2 == 0:
        print("Can't divide by zero!")
        sys.exit(1)
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, logfile)
timestamp = datetime.now().isoformat()
user = os.getenv("USER","anonymous")

#prints the result
print(f"The result is = {result}")

#use try to treat premission error handling to save the log
try:
    #it's most commom to go to this way instead of using print
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operation}: {n1}, {n2} = {result}\n")
except PermissionError as e:
    #TODO: logging
    print(f"{str(e)}.")
    sys.exit(1)
    
#this would be like using print to save the logs:
#print(f"{operation}: {n1}, {n2} = {result}", file=open(filepath, "a"))
