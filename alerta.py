#!/usr/bin/env python3

"""Weather alert. 

Based on the temperature and humidity index given, returns to the user an
alert of the heat conditions, using the heat index formula:

For weather above 80 F:

Heat Index = 0.5 × (Temp + 61 + ((Temp − 68) × 1.2) + (Humidity × 0.094))

Heat index above 54 degrees: EXTREME DANGEROUS HEAT ALERT!
Heat index between 40 and 54 degrees: DANGEROUS HEAT ALERT!
Heat index between 32 and 40 degrees: Potencially danger heat!
Heat index between 27 and 32 degrees: The Weather is Unconfortably Hot
Heat index under 27 degrees: The Weather is Hot, but not Uncomfortable

For Weather under 80 F:

Temperature between 65 and 80 F: The Weather is just fine
Temperature between 50 and 65 F: The Weather is Somewhat Cold
Temperature between 32 and 50 F: The Weather is Pretty Cold
Temperature under 32 F: THE WEATHER IS FREEZING!!!

Usage:
$ python3 alerta.py
Type the temperature, in Celsius or Farenheit: 35, c 
Type the humidity, in percentage: 70

$ python3 alerta.py
Type the temperature, in Celsius or Farenheit: 95, f 
Type the humidity, in percentage: 70
"""

__version__ = "0.2.0"
__author__ = "Jenny DeVito"
__license__ = "Unlicense"

import sys

data = []
data = input("Type the temperature, in Celsius (C) or Fahrenheit (F). \n"
    "Separated by a comma: "
    )
    
data = data.split(",")
if len(data) != 2:
    print("Please, follow this script instructions!")
    print("Type the temperature, in Celsius (C) or Fahrenheit (F)")
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

humidity = -11
while humidity < 0 or humidity > 100:
    humidity = int(input("Type the humidity index, in percentage: "))
    if humidity < 0 or humidity > 100:
        print("\nPlease, type a valid number!")

temp = 0
if scale_temp == "C":
    temp = (initial_temp * (9 / 5)) + 32
else: 
    temp = initial_temp

if temp > 80:
    heat_index = 0.5 * (temp + 61 + ((temp - 68) * 1.2) + (humidity * 0.094))

    if heat_index > 54:
        print("\nEXTREME DANGEROUS HEAT ALERT!\n")
    elif heat_index > 40 and heat_index <= 54:
        print("\nDANGEROUS HEAT ALERT!\n")
    elif heat_index > 32 and heat_index <= 40:
        print("\nPotencially dangerous heat!\n")
    elif heat_index > 27 and heat_index <= 32:
        print("\nThe Weather is Uncomfortably Hot\n")
    else:
        print("\nThe Weather is Hot, but not Uncomfortable\n")

elif temp > 65 and temp <= 80:
    print("\nThe Weather is just fine\n")

elif temp > 50 and temp <= 65:
    print("\nThe Weather is Somewhat Cold\n")

elif temp > 32 and temp <= 50:
    print("\nThe Weather is Pretty Cold\n")

elif temp < 32:
    print("\nTHE WEATHER IS FREEZING!!!\n")
