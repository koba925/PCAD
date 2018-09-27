#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import setrecursionlimit
from functools import lru_cache


@lru_cache()
def lcs(s1, s2):
    if s1 == "" or s2 == "":
        return 0

    first = s1[0]
    rest = s1[1:]

    index = s2.find(first)
    if index == -1:
        return lcs(rest, s2)
    else:
        return max(lcs(rest, s2[index+1:]) + 1, lcs(rest, s2))


def main():
    setrecursionlimit(10000)

    q = int(input())

    for _ in range(q):
        x = input()
        y = input()
        print(lcs(x, y))


if __name__ == '__main__':
    main()
