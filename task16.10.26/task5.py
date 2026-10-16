#!/usr/bin/python3
print('enter <stop> to stop')
sequences = []
while (seq := input('enter sequence:')) != 'stop':
    sequences.append(seq)
k = int(input('enter k:'))
for i, seq1 in enumerate(sequences, 1):
    for j, seq2 in enumerate(sequences, 1):
        if seq1[-k:] == seq2[:k]:
            print(f'{i} - {j}')

