#!/usr/bin/python3
print('enter <stop> to stop')
sequences = []
while (seq:=input('input sequence:')) != 'stop':
    sequences.append(seq)
for seq1 in sequences:
    for seq2 in sequences:
        count = 0
        for i, c in enumerate(seq1):
            if c != seq2[i]:
                count += 1
        print(count, end=' ')
    print('\n', end='')
