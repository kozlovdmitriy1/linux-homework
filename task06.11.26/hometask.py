#!/usr/bin/python3

dna1 = input()
dna2 = input()

max_match = 0
best_intervals = []
for i in range(len(dna1)-len(dna2)+1):
    count = 0
    for j in range(len(dna2)):
        if dna1[i+j]==dna2[j]:
            count += 1
    if count == max_match:
        best_intervals.append([i+1, i+len(dna2)])
    elif count > max_match:
        max_match = count
        best_intervals = [[i+1, i+len(dna2)]]

print(max_match)
print(best_intervals)

