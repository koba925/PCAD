#! /usr/local/bin/python3
# coding: utf-8


def swap(w, i, j):
    tmp = w[i]
    w[i] = w[j]
    w[j] = tmp


def min_weight(w):
    ws = sorted(w)
    # print(ws)
    # print(w)
    weight = 0
    for i in reversed(range(len(w))):
        j = w.index(ws[i])
        # print(i, j)
        if i != j:
            weight += w[i] + w[j]
            swap(w, i, j)
        # print(ws)
        # print(w)
    return weight


def main():
    n = int(input())
    w = [int(x) for x in input().split()]
    print(min_weight(w))


main()
