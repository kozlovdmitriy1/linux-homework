#!/usr/bin/python3
import sys
number = sys.argv[1]
print(f'{sum([int(c) for c in number])}, {number[::-1]}')
