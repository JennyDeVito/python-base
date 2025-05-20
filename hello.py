#!/usr/bin/env python3
"""Multi language hello world

Depending on the language in the system's configuration the program shows the
correspoding message.

Usage:
you should have the language variable properly configurated:

    export LANG=pt_BR

Execution:

    python3 hello.py
    or
    ./hello.py

"""

#metada
__version__ = "0.0.1"
__author__ = "Jenny DeVito"
__license__ = "Unlicense"

#main program
import os
current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if  current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "\u00A1Hola, Mundo!"
elif current_language == "ja_JP":
    msg = "Konichiwa, Sekai!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)
