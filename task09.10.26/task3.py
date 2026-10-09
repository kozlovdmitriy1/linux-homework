#!/usr/bin/python3

import sys

dna = sys.argv[1].upper()

compl = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

print(''.join([compl[c] for c in dna[::-1]]))
