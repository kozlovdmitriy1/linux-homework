#!/usr/bin/python3
import sys
a, b = int(sys.argv[1]), int(sys.argv[2])
print(f'{a} + {b} = {a+b}', f'{a} - {b} = {a-b}', f'{a} * {b} = {a*b}', sep='\n')
