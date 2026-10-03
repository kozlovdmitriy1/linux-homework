#!/usr/bin/python3
import sys
seconds = int(sys.argv[1])
print(f'{seconds//3600}:{seconds%3600//60}:{seconds%60}')

