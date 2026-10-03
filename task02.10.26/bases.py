#!/usr/bin/python3
import sys
number = sys.argv[1]
number = int(number, 0)
print(bin(number), oct(number), int(number), hex(number))
