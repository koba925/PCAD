#! /usr/local/bin/python3
# coding: utf-8

def print_it(v):
    it = iter(v)
    while True:
        try:
            print(next(it), end="")
        except StopIteration:
            break
    print()

def iter_sample():
    v = [int(x) for x in input().split()]

    print_it(v)

    it = iter(v)
    v2 = []
    next(it)
    v2.append(3)
    v2.append(next(it) + 1)
    v2.append(next(it))
    v2.append(next(it))

    print_it(v2)

    it = iter(v)
    v3 = []
    for i, x in enumerate(v):
        if i == 0:
            v3.append(3)
        elif i == 1:
            v3.append(x + 1)
        else:
            v3.append(x)

    print_it(v3)

iter_sample()
