#!/usr/bin/env python3
"""Multi language hello world

Depending on the language in the system's configuration the program shows the
correspoding message.

Usage:
you should have the language variable properly configurated:

    export LANG=pt_BR

Or inform through CLI argument '--lang='

Or inform through user's input.

Execution:

    python3 hello.py
    or
    ./hello.py

"""

#metada
__version__ = "0.1.3"
__author__ = "Jenny DeVito"
__license__ = "Unlicense"

#main program
import os
import sys

#dict that contains the language value the user inputted to the system
arguments = {
    "lang": None,
    "count": 1,
}

#iteration on the received CLI command with error handling - for now only typo
for arg in sys.argv[1:]:
    #TODO: tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
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

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "\u00A1Hola, Mundo!",
    "ja_JP": "Konichiwa, Sekai!",
    "fr_FR": "Bonjour, Monde!"
}

print(msg[current_language] * int(arguments["count"]))
