#!/usr/bin/python3

import sys

num = int(sys.argv[1])
for i in range(1, num+1):
    for j in range(1, num+1):
        print(i*j, end=' ')
    print('\n', end='')

