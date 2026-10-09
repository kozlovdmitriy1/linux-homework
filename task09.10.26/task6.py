#!/usr/bin/python

alph1 = input().split()
num = int(input())

def string(alph, n):
    if n == 1:
        return alph
    else:
        strings = []
        for c in string(alph, n-1):
            for c1 in alph:
                strings.append(c+c1)
        return strings

print(*string(alph1, num), sep='\n')

