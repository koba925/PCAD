#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import maxsize


def count_2(m1, m2):
    assert m1[1] == m2[0]
    return m1[0] * m1[1] * m2[1]


def result_2(m1, m2):
    return (m1[0], m2[1])


def irange(start, stop=None):
    if stop:
        return range(start, stop + 1)
    else:
        return range(start + 1)


def count(m):

    lm = len(m)
    if lm == 1:
        return m[0], 0

    cache = [[None] * (lm + 1) for _ in irange(lm)]
    for i in range(lm):
        cache[1][i + 1] = (m[i], 0)

    for n in irange(2, lm):
        # print("n:", n)
        for i in irange(1, lm - n + 1):
            # print("i:", i)
            min_count = maxsize
            min_result = (0, 0)
            for j in irange(1, n - 1):
                m1, c1 = cache[j][i]
                m2, c2 = cache[n - j][i + j]
                # print("j:{} m1:{} c1:{} m2:{} c2:{}".format(
                #     j, m1, c1, m2, c2))
                m3, c3 = result_2(m1, m2), count_2(m1, m2)
                c = c1 + c2 + c3
                if c < min_count:
                    min_count = c
                    min_result = m3
            cache[n][i] = (min_result, min_count)

    return min_result, min_count


# print(count([(2, 3), (3, 3), (3, 2), (2, 4), (4, 1)]))
# print(count([(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]))
# exit()


def main():
    n = int(input())

    m = []
    for _ in range(n):
        m.append(tuple(int(x) for x in input().split()))
    _, c = count(m)
    print(c)


if __name__ == '__main__':
    main()
