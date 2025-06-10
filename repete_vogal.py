#!/usr/bin/env python 3
"""Repete vowels.

This program doubles the vowels of the words typed by the user.

Example:

$ python3 repete_vogal.py
'Type a word (or ENTER to quit):' Python
'Type a word (or ENTER to quit):' Casa
'Type a word (or ENTER to quit):' <enter>
Pythoon
Caasaa
"""

__version__ = "0.1.1"
__author__ = "Jenny DeVito"
__license__ = "Unlicense"

import sys

words = []
while True:
    word = (input("Type a word (or ENTER to quit): ")).lower().strip()
    if word.isdigit():
        print("You must type a word!")
    else:
        words.append(word)  
    if word == "":
        break
    
#print(words) #debug

vowels = ("a", "e", "i", "o", "u", "ã", "õ", "á", "é", "í", "ó", "ú", "ê", "ô")

for index in range(0, len(words)):
    #print(index) #debug
    new_word = ""
    for letter in words[index]:
        #TODO: remover acento usando funcão
        if letter in vowels:
            #print(letter) #debug
            new_word = new_word + letter
        #print(letter) #debug
        new_word = new_word + letter
    print(new_word)


"""Teacher's solution:

words = []

while True:
    word = input().strip()
    if not word:
        break

    final_word = ""
    for letter in word:
        #if ternário
        final_word += (
            letter * 2
            if letter.lower() in "aeiouãõáéíóúêô"
            else letter
        )

    words.append(final_word)

print(*words, sep="\n")
"""
