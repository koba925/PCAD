#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import maxsize


def count_2(m1, m2):
    assert m1[1] == m2[0]
    return m1[0] * m1[1] * m2[1]


def result_2(m1, m2):
    return (m1[0], m2[1])


def count(m):
    assert len(m) > 0

    if len(m) == 1:
        return m[0], 0
    elif len(m) == 2:
        return result_2(m[0], m[1]), count_2(m[0], m[1])

    min_count = maxsize
    min_result = (0, 0)
    for i in range(1, len(m)):
        m1, c1 = count(m[:i])
        m2, c2 = count(m[i:])
        m3, c3 = result_2(m1, m2), count_2(m1, m2)
        c = c1 + c2 + c3
        if c < min_count:
            min_count = c
            min_result = m3

    return min_result, min_count

# print(count([(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]))


def main():
    n = int(input())

    m = []
    for _ in range(n):
        m.append(tuple(int(x) for x in input().split()))
    _, c = count(m)
    print(c)


if __name__ == '__main__':
    main()
