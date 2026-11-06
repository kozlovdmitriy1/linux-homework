#!/usr/bin/python3

def read_file(filename):
    records = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
    
            if line.startswith('>'):
                record = {
                        'metadata': line[1:],
                        'data': ''
                    }
    
                records.append(record)
    
            else:
                records[-1]['data'] += line
    return records

def gc_count(dna):
    return (dna.count('G') + dna.count('C'))/len(dna)*100

for c in read_file('gene.fna'):
    print(gc_count(c['data']))
print('-'*20)
for c in read_file('cds.fna'):
    print(gc_count(c['data']))

def find_seq(dna, seq):
    positions = []
    for i in range(len(dna)-len(seq)):
        if dna[i:i+len(seq)] == seq:
            positions.append(i)
    return len(positions), positions

print(*find_seq(read_file('gene.fna')[0]['data'], input('input sequence')))

