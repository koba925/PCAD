#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import setrecursionlimit
from functools import lru_cache


def lcs(s1, s2):

    @lru_cache()
    def rec(i1, i2):
        nonlocal s1, l1, s2, l2

        if i1 == l1 or i2 == l2:
            return 0

        if s1[i1] == s2[i2]:
            return rec(i1 + 1, i2 + 1) + 1
        else:
            return max(rec(i1 + 1, i2),
                       rec(i1, i2 + 1))

    l1 = len(s1)
    l2 = len(s2)
    return rec(0, 0)


def main():
    setrecursionlimit(10000)

    q = int(input())

    for _ in range(q):
        x = input()
        y = input()
        print(lcs(x, y))


if __name__ == '__main__':
    main()
