#!/usr/bin/python3

def filter_expression(values, threshold=5.0):
    new = []
    for c in values:
        if c > int(threshold):
            new.append(c)
    return new

l = [int(c) for c in input().split()]
thresh = int(input())
print(filter_expression(l, thresh))
