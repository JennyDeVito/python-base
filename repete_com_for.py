#!/usr/bin/env python3

"""Script to explore loops and repetitions in Python using for"""

__version__ = "0.1.0" 

"""list(range()): creates a list and consumes memory space for every
numbers[i] slot"""

#numbers = list(range(1,700))

"""when you create the numbers' sequence without making a actual list the
range only uses 3 memory slots: 1) slot for the start number, 2) slot for the
next number and 3) slot for the stop number - the range command internally
implemments the algorithm by itself and when the next number is equal the last
number it stops"""

numbers = range(1, 11) #(first, last+1, step)

"""FOR: range sequences are also iterable"""

for number in numbers:
    if number % 2 == 0:
        print(number)
    else:
        continue
    print(f"mais código com {number}")

"""FOR: using break to interrupt a iteration"""

data = {}

for line in open("post.txt"):
    if line == "---\n":
        break
    key, value = line.split(":")
    data[key] = value.strip()

print(data)
print(data["title"])

"""for loops / laco for"""

original = [1, 2, 3]
doubled = []

for n in original:
    doubled.append(n * 2)

print(doubled)

"""functional programming"""
#uses list comprehension
doubled = [n * 2 for n in original]
print(doubled)

#dict comprehension
data = {
    line.split(":")[0]: line.split(":")[1].strip() 
    for line in open("post.txt") 
    if ":" in line
    }
print(data)

#conventional way
data = {}
for line in open("post.txt"):
    if ":" in line:
        key, value = line.split(":")
        data[key] = value.strip()
print(data)
