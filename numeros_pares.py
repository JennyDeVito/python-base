#!/usr/bin/env python3

"""Prints the even numbers until 200

Usage: 

$ python3 numeros_pares.py
2
4
6
8
...
200
"""
__version__ = "0.1.0"
__author__ = "Jenny DeVito"

for n in range(1, 201):
    if n % 2 == 0:
        print(n)
