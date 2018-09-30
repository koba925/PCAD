#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def lcs(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    c = [0] * (l2 + 1)
    for i1 in range(l1):
        cprev = c[:]
        for i2 in range(l2):
            if s1[i1] == s2[i2]:
                c[i2 + 1] = cprev[i2] + 1
            elif c[i2 + 1] < c[i2]:
                c[i2 + 1] = c[i2]
    return c[-1]


def main():
    q = int(input())

    for _ in range(q):
        x = input()
        y = input()
        print(lcs(x, y))


if __name__ == '__main__':
    main()
