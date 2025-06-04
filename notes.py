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

__version__ = "0.1.1"

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

#read notes
if arguments[0] == "read":
    #checks the number of arguments
    if len(arguments) != 2:
        print("Invalid number of arguments!")
        print("read 'tagname'")
        sys.exit(1)

    for line in open(filepath):
        #unpacks the line into 3 variables
        title, tag, text = line.split("\t")
        #compares the given tag with the tags in the notebook
        if tag.lower() == arguments[1].lower():
            print(f"Title: {title}")
            print(f"Text: {text}")
            print("-" * 30)
            print()
            
#write notes
if arguments[0] == "new":
    try:
        title = arguments[1]
    except IndexError as e:
        print(f"[Error] {str(e)}.")
        print("You must give a title to your note!")
        print("Try: $ python3 notes.py new 'Title'")
        sys.exit(1)
    text = [
        f"{title}",
        input("tag: ").strip(),
        input("text: \n").strip(),
    ]

#by convention the field separator will be \t - tsv
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")
