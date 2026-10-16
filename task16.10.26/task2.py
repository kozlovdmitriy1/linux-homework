#!/usr/bin/python3

reference = input('input reference:')
sample = input('input sample:')

for pos, letter in enumerate(reference):
    if letter != sample[pos]:
        print(f'{pos+1}: {letter} > {sample[pos]}')
