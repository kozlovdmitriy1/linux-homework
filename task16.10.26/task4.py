#!/usr/bin/python3

grouth = []
grouth.append(map(int, input('input colony 1 od').split()))
grouth.append(map(int, input('input colony 2 od').split()))
grouth.append(map(int, input('input colony 3 od').split()))
threshold = 5
for colony in grouth:
    for j, od in enumerate(colony):
        if od >= threshold:
            print(j)
            break
    else:
        print('отсутствует')

