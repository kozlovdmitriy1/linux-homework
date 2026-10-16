#!/usr/bin/python3

dna_list = []
while (dna := input()) != 'STOP':
    for c in dna:
        if c not in 'ATGC':
            break
    else:
        dna_list.append(len(dna))
        continue
    print('invalid dna')
print(len(dna_list))
print(*dna_list)
