#!/usr/bin/env python3

"""Weather alert. 

Based on the temperature and humidity index given, returns to the user an
alert depending on the conditions:

Temperature above 45 degrees: Alert! Extreme Heat Danger
If temperature times 3 is higher or equal the humidity index: Alert! 
Humid Heat Danger
Temperature between 10 and 30 degrees: Normal Weather
Temperature between 0 and 10 degrees: Cold Weather
Temperature below 10 degrees: Extreme Cold Weather

Usage:
$ python3 alerta.py
Type the temperature, in Celsius or Farenheit: 35, c 
Type the humidity, in percentage: 70

$ python3 alerta.py
Type the temperature, in Celsius or Farenheit: 95, f 
Type the humidity, in percentage: 70
"""

__version__ = "0.1.0"
__author__ = "Jenny DeVito"
__license__ = "Unlicense"

import sys

data = []
data = input("Type the temperature, in Celsius (C) or Farenheit (F). \n"
    "Separated by a comma: "
    )
    
data = data.split(",")
if len(data) != 2:
    print("Please, follow this script instructions!")
    print("Type the temperature, in Celsius (C) or Farenheit (F)")
    print("Example: '35, C' or '95, F'")
    print("Try again")
    sys.exit(1)

if not data[0].replace(".","").replace("-","").isdigit():
    print(f"Invalid Temperature {data[0]}. Try again.")
    sys.exit(1)

initial_temp = data[0].strip()
if "." in initial_temp:
    initial_temp = float(data[0])
else:
    initial_temp = int(data[0])
    
correct_temp = ("C", "F")
scale_temp = data[1].upper().strip()
if scale_temp not in correct_temp:
    print("You must type 'c' or 'f' after the temperature!")
    print("Try again")
    sys.exit(1)

try:
    humidity = int(input("Type the humidity index, in percentage: "))
except ValueError as e:
    print(f"Type an integer number! {str(e)}")
    print("You can try once again")
    try:
        humidity = int(input("Type the humidity index, in percentage: "))
    except ValueError as e:
        print(f"That was your last chance! {str(e)}")
        print("Start over!")
        sys.exit(1)

temp = 0
if scale_temp == "F":
    temp = (initial_temp - 32) * (5 / 9)
else: 
    temp = initial_temp

critical = temp * 3

if critical >= humidity:
    print("\nHUMID HEAT ALERT!\n")
elif temp > 45:
    print("\nEXTREME HEAT ALERT!\n")
elif temp > 30 and temp <= 45:
    print("\nThe Weather is Hot\n")
elif temp > 10 and temp <= 30:
    print("\nThe Weather is Normal\n")
elif temp > 0 and temp <= 10:
    print("\nThe Weather is Cold\n")
elif temp < 0:
    print("\nEXTREME COLD ALERT!\n")
