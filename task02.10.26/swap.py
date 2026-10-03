#!/usr/bin/python3
import sys
num1, num2 = sys.argv[1], sys.argv[2]
print(f'id of \'{num1}\' pre-swap: {id(num1)}\nid of \'{num2}\' pre-swap: {id(num2)}')
num1, num2 = num2, num1
num1, num2 = int(num2), int(num1)
print(f'id of \'{num1}\' post-swap: {id(num1)}\nid of \'{num2}\' post-swap: {id(num2)}')
