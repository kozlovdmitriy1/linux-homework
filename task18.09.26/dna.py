#!/usr/bin/python3
import sys
dna = sys.argv[1]
complimentary_strain = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
print(''.join([complimentary_strain[c] for c in dna[::-1]]), dna.replace('T', 'U'), dna.find('ATG'))
