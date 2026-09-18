#!/usr/bin/python3
import sys
oligo = sys.argv[1]
print(f'Sequence: {oligo}', f'Length: {len(oligo)}', f'A: {oligo.count('A')}', f'T: {oligo.count('T')}', f'G: {oligo.count('G')}', f'C: {oligo.count('C')}', f'GC: {(oligo.count('G')+oligo.count('C'))/len(oligo)}', sep='\n')
