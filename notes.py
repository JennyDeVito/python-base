#!/usr/bin/env python3

"""Bloco de notas

$ python3 notes.py new "Minha Nota"
tag: tech
text:
Anotacão geral sobre carreira de tecnologia.

$ python3 notes.py read tech
...
...
"""

__version__ = "0.1.2"

import os
import sys

#filepath and file where the notes will be written
path = os.curdir
filepath = os.path.join(path, "notes.txt")

#reads the CLI arguments
arguments = sys.argv[1:]

#valid comands
cmds = ("read", "new")

#validating if there are CLI arguments
if not arguments:
    print(f"You must give the arguments! {cmds}")
    sys.exit(1)

#validating if the arguments are correct
if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

while True:

    #read notes
    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Type the tag of your note: ").strip().lower()

        #notes reading
        for line in open(filepath):
            #unpacks the line into 3 variables
            title, tag, text = line.split("\t")
            #compares the given tag with the tags in the notebook
            if tag.lower() == arg_tag:
                print(f"Title: {title}")
                print(f"Text: {text}")
                print("-" * 30)
                print()
                
    #write notes
    if arguments[0] == "new":
        try:
            title = arguments[1]
        except IndexError:
            title = input("Type the title of your note: ").strip().title()
            
        text = [
            f"{title}",
            input("tag: ").strip(),
            input("text: \n").strip(),
        ]

    #by convention the field separator will be \t - tsv
        with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")

    cont =  input("Do you want to continue? [y]").strip().lower()

    if cont != "y":
        break
