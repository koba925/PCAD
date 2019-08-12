#! /usr/local/bin/python3
# coding: utf-8

from itertools import product
from math import inf
from sys import setrecursionlimit

setrecursionlimit(10000)

ws = []
min_weight = inf


def swap(w, i, j):
    tmp = w[i]
    w[i] = w[j]
    w[j] = tmp


def try_next(w, total, hand):
    global min_weight

    # print("try_next", w, total, hand)

    if total > min_weight:
        return

    if w == ws:
        min_weight = min(total, min_weight)
        print("new record", min_weight, total, hand)
        return

    for i, j in product(range(len(w)), range(len(w))):
        if i >= j:
            continue
        wnew = w[:]
        swap(wnew, i, j)
        hnew = hand[:]
        hnew.append((i, j))
        try_next(wnew, total + w[i] + w[j], hnew)

    return


def first_try(w):
    global ws

    weight = 0
    for i in reversed(range(len(w))):
        j = w.index(ws[i])
        if i != j:
            weight += w[i] + w[j]
            swap(w, i, j)
    return weight


def main():
    global ws, min_weight

    n = int(input())
    w = [int(x) for x in input().split()]
    ws = sorted(w)

    min_weight = first_try(w[:])
    print("first_try", min_weight)
    try_next(w, 0, [])
    print(min_weight)


main()
