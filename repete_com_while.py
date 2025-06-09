#!/usr/bin/env python3

"""Script to explore loops and repetitions in Python using while"""

__version__ = "0.1.0"

#while the condition is True do something

n = 0
#while True: #infinity loop, main loop
while n < 101: #loop w/ a stop condition
	if n >= 40 and n <= 60:
		n += 1 #increments to avoid a deadlock
		continue
	print(n)
	n += 1

n = 0
while n < 101:
	if n % 2 != 0:
		n += 1
		continue
	print(n)
	n += 1

while True:
	
