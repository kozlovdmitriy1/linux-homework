#!/usr/bin/python3
import sys
deposit, rate, period = map(int, sys.argv[1:])
for _ in range(period):
    deposit += deposit*rate/100
print(f'{deposit:_.2f}'.replace('_', ' '))
