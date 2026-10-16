#!/usr/bin/python3

rna = input('input rna:')
codons = [rna[i:i+3] for i in range(0, len(rna), 3)]
count = 0
for c in codons:
    if c in ['UAA', 'UAG', 'UGA']:
        print(f'Количество кодирующих кодонов: {count}\nСтоп-кодон: {c}')
        break
    count += 1
else:
    print('Стоп-кодон не найден')
