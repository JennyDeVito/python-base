"""Room reservation manager. 

Shows the user a list of the available rooms and their prices:

#   Room    Price
1,Master Suite,500
2,Family Room,200
3,Single Room,100
4,Simple Room,50

Then asks the user their name, room number to be reserved and amount of days of
stay:

In the end shows the estimated amount to be paid and do the reservation:

If the user tries to book a room already booked, the script shows a message
saying that it is not possible: 

The reservation will be saved in a reserva.txt file.
"""

__version__ = "0.1.1"
__author__ = "Jenny DeVito"
__license__ = "Unlicense"

import os
import sys
import logging
from logging import handlers

"""LOG CONFIGURATION: log boilerplate"""
#TODO: usar funcão
#TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("Jenny", log_level)
ch = logging.StreamHandler() #sends the log message to the console
ch.setLevel(log_level) #console handler
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d "
    "f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)

"""MAIN PROGRAM"""
#stablishing the filepaths
path = os.curdir
read_fp = os.path.join(path, "quartos.txt")
write_fp = os.path.join(path, "reserva.txt")

#printing the header
print()
print("{:^80}".format(f"WELCOME TO THE RESERVATION SYSTEM"))
print("{:^80}".format(f"ROOMS: AVAILABLE 🟢 | NOT AVAILABLE 🔴"))
print()

#TODO: usar funcao para ler os arquivos
#accessing the database
booked = {}
try:
    for line in open(write_fp):
        client_name, room_num, days = line.strip().split(",")
        booked[int(room_num)] = {
            "name": client_name,
            "days": int(days)
        }
except FileNotFoundError:
    log.error("Reservation file doesn't exist")
    sys.exit(1)

rooms = {}
try:
    for line in open(read_fp):
        code, room_name, price = line.strip().split(",")
        rooms[int(code)] = {
            "name": room_name,
            "price": float(price), #TODO: Decimal
            "available": False if int(code) in booked else True
        }
except FileNotFoundError:
    log.error("Room file doesn't exist")
    sys.exit(1)

auxt_room = "ROOM NAME"
auxt_price = "PRICE"
auxt_av = "AVAILABLE"
print(f"NUMBER  {auxt_room:^12} {auxt_price:^10} {auxt_av:^9}")
#printing the information on screen
for code, data in rooms.items():
    available = "🔴" if not data["available"] else "🟢"
    #TODO: substituir casa decimal por virgula
    print(
        f"{code:^6}: {data['name']:^12}"
        f" {data['price']:^6.2f} USD {available:^9}"
    )

#message in case all rooms are booked - kills the program
if len(booked) == len(rooms):
    print("{:^80}".format(f"THE HOTEL IS FULL"))
    print()
    sys.exit(0) #it is not an error

#message to guide the user to make the reservation
print()
print("{:^80}".format(f"TO MAKE A RESERVATION, PLEASE:"))
print()

#TODO: usar funcao para ler os inputs
#asks the user for information and do the validation
name = input("Type your name: ").strip()
if name.isdigit():
    print("You must type letters!")
    sys.exit(1)

try:
    room = int(input("Type the number of the room you want: "))
    if not rooms[room]["available"]:
        print(f"Room {room} isn't available.")
        sys.exit(1)
except ValueError:
    log.error("You must type a number!")
    sys.exit(1)
except KeyError:
    print("The room {room} doesn't exist!")
    sys.exit(1)

try:
    stay = int(input("Type the number of days do you wish to stay: "))
except ValueError:
    log.error("You must type a number!")
    sys.exit(1)

#group the info into new variables to make it easy to put it into the message
room_name = rooms[room]["name"]
amount = rooms[room]["price"] * stay

#creates a list with the values to write on the reserva.txt file
reservation = [name, str(room), str(stay)]

#confirmation message
print()
print("{:^80}".format(f"CONFIRMATION"))
print()
print(f"{name}, you choose the {room_name} to stay for {stay} day(s)")
print(f"The amount to be paid starts in {amount:.2f} USD")
print()

#confirmation
confirm = ("y", "yes", "s", "sim")
if input("Do you confirm? [Y/n]: ").strip().lower() in confirm:
    #write on the reserva.txt file
    with open(write_fp, "a") as file_:
        file_.write("," .join(reservation) + "\n")
else:
    print("{:^80}".format(f"RESERVATION CANCELED"))
    sys.exit(0)

#footer note    
print("{:^80}".format(f"ENJOY YOUR STAY"))
print("{:^80}".format(f"\N{party popper} \N{party popper} \N{party popper}"))
print()
