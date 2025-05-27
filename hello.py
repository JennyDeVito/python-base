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
__version__ = "0.1.2"
__author__ = "Jenny DeVito"
__license__ = "Unlicense"

#main program
import os
current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "\u00A1Hola, Mundo!",
    "ja_JP": "Konichiwa, Sekai!",
    "fr_FR": "Bonjour, Monde!"
}

print(msg[current_language])
