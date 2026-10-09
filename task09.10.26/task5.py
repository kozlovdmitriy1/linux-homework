#!/usr/bin/python3

import sys

dna, seq = sys.argv[1:]

indexes = []
for i in range(len(dna)):
    if dna[i:i+len(seq)] == seq:
        indexes.append(i+1)

print(*indexes)
