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

$ prefixcalc.py
operation: sum
n1: 5
n2: 4
Log filename: filename
The result is = 9
Type y to continue, any other key to end:

The results will be saved in filename.log. You can use the same file for the
results, just type the same name and the program will add the results in order.

Errors will be saved in log_prefixcalc.log and also printed on the screen.
"""

__version__ = "0.1.5"
__author__ = "Jenny DeVito"
__license__ = "Unlicense"

import os
import sys
from datetime import datetime
import logging
from logging import handlers

"""LOG CONFIGURATION"""
#TODO: usar funcão
#TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("Jenny", log_level)
ch = logging.StreamHandler() #sends the log message to the console
fh = handlers.RotatingFileHandler(
    "log_prefixcalc.log",
    maxBytes=2**20, #the ideal is something around 2**20 or 1Mib
    backupCount=10, #teacher suggested 10 but is to be evaluated
)
ch.setLevel(log_level) #console handler
fh.setLevel(log_level) #file handler
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d "
    "f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
fh.setFormatter(fmt)
log.addHandler(ch)
log.addHandler(fh)

"""MAIN PROGRAM"""


#reads CLI arguments from the program name
arguments = sys.argv[1:]

while True:
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
        print("Invalid number of arguments")
        print("Example: 'sum 7 6 --logfilename'")
        #sys.exit(1) tells the terminal that the program ended in error
        sys.exit(1) 
    #unpacks arguments into operation and numbers into a list nums
    operation, *nums, logfile = arguments

    #redefine the arguments list to avoid an infinite loop with the CLI args
    arguments = []

    #adjusts the log filename so it results in a proper filename with a .log 
    #in the end
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
        log.error("%s", str(e))
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
        try:
            result = n1 / n2
        except ZeroDivisionError as e:
            log.error("Can't divide by zero!")
            sys.exit(1)

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
            file_.write(
                f"{timestamp} - {user} - {operation}: {n1}, {n2} = {result}\n"
            )
    except PermissionError as e:
        log.error("You don't have permission to save files on this folder! %s",
        str(e)
        )
        sys.exit(1)
        
    #this would be like using print to save the logs:
    #print(f"{operation}: {n1}, {n2} = {result}", file=open(filepath, "a"))

    cont = input("Type y to continue, any other key to end: ")
    
    if cont != "y":
        break

    #another option is:
    #if input("Press ENTER to continue or any other key to end: ")
        #break
