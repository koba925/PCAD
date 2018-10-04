#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import maxsize


def irange(start, stop=None):
    if stop:
        return range(start, stop + 1)
    else:
        return range(start + 1)


def count(ms):
    n = len(ms)

    p = [0] * (n + 1)
    for i in range(n):
        p[i] = ms[i][0]
        p[i + 1] = ms[i][1]

    m = [[None] * (n + 1) for _ in irange(n)]
    for i in irange(1, n):
        m[i][i] = 0
    for l in irange(2, n):
        for i in irange(1, n - l + 1):
            j = i + l - 1
            m[i][j] = maxsize
            for k in irange(i, j - 1):
                m[i][j] = min(
                    m[i][j],
                    m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                )

    return m[1][n]


def main():
    n = int(input())

    m = []
    for _ in range(n):
        m.append(tuple(int(x) for x in input().split()))
    c = count(m)
    print(c)


if __name__ == '__main__':
    main()
