#! /usr/bin/env python3
# # -*- coding: utf-8 -*-

from sys import stdin


def sort_of_trees(n):
    s = 1
    for k in range(n):
        s *= (n - k) * (2 * k - (k - 1))
    return s


for n in range(1, 11):
    print(n, ":", sort_of_trees(n))
