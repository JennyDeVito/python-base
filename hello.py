#!/usr/bin/env python3
"""Multi language hello world

Depending on the language in the system's configuration the program shows the
correspoding message.

Usage:
you should have the language variable properly configurated:

    export LANG=pt_BR

Or inform through CLI argument '--lang=' '--count='

Or inform through user's input.

Execution:

    python3 hello.py --lang=value --count=integer
    or
    ./hello.py --lang=value --count=integer

"""

#metada
__version__ = "0.1.4"
__author__ = "Jenny DeVito"
__license__ = "Unlicense"

#main program
import os
import sys
import logging

#TODO: usar funcão
#TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("Jenny", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d "
    "f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)

#dict that contains the language value the user inputted to the system
arguments = {
    "lang": None,
    "count": 1,
}

#iteration on the received CLI command with error handling - for now only typo
for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use '=', you passed %s, try with --lang=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)
        
    key = key.lstrip("-").strip()
    value = value.strip()
    #validation
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit(1)
    arguments[key] = value

#use the system's language, if None, use the language provided by the user
#in the CLI, if None, tells the user to input a language
current_language = arguments["lang"]
if current_language is None:
    #TODO: usar repeticão
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")
        arguments["count"] = input("Type how many times to print the message: ")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "\u00A1Hola, Mundo!",
    "ja_JP": "Konichiwa, Sekai!",
    "fr_FR": "Bonjour, Monde!"
}

"""try with default value
dictionaries has a get objet, so it is easy to obtain results from it
it has a default value to choose from if the users inputted a wrong value
but it has no error handling"""
#message = msg.get(current_language, msg["en_US"])

#EAFP
try:
    message = msg[current_language]
except KeyError as e:
    log.error(
        "Language is invalid, please choose from: %s ", msg.keys()
    )
    sys.exit(1)

try:
    times = int(arguments["count"])
except ValueError as e:
    log.error(
        "You didn't passed a integer number, try '--count=5'"
        " %s",
        str(e)
    )
    sys.exit(1)

print((message + "\n") * times)
