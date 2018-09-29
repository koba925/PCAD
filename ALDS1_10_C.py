#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import setrecursionlimit
from functools import lru_cache


def lcs(s1, s2):

    l1 = len(s1)
    l2 = len(s2)
    c = [[0] * (l2 + 1) for _ in range(l1 + 1)]

    maxl = 0
    s1 = " " + s1
    s2 = " " + s2

    for i1 in range(1, l1 + 1):
        for i2 in range(1, l2 + 1):
            if s1[i1] == s2[i2]:
                c[i1][i2] = c[i1 - 1][i2 - 1] + 1
            else:
                c[i1][i2] = max(c[i1 - 1][i2],
                                c[i1][i2 - 1])
            maxl = max(maxl, c[i1][i2])

    return maxl


def main():
    setrecursionlimit(10000)

    q = int(input())

    for _ in range(q):
        x = input()
        y = input()
        print(lcs(x, y))


if __name__ == '__main__':
    main()
