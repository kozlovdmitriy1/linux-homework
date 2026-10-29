#!/usr/bin/python3

def is_valid_dna(dna):
    for c in dna:
        if c not in 'ATGC':
            return False
    if len(dna) == 0:
        return False
    return True
def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        return None
    if not is_valid_dna(s1) or not is_valid_dna(s2):
        return None
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1
    return dist

print(hamming_distance(input(), input()))

