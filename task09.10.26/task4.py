#!/usr/bin/python3

import sys

dna = sys.argv[1].upper()

print((dna.count('G') + dna.count('C'))/len(dna))
