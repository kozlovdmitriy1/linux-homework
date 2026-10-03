#!/usr/bin/python3
import sys
string = sys.argv[1]
print(len(string), string[0], string[-1], string[len(string)//2], string[1::2], string[::-1], string==string[::-1])
