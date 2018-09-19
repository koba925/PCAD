# /usr/bin/env python3
# -*- coding: utf-8 -*-

from math import floor


def parent_node(k):
    return k // 2


def left_node(k):
    return 2 * k


def right_node(k):
    return 2 * k + 1


def main():
    H = int(input())
    elems = [0] + [int(x) for x in input().split()]

    for k in range(1, H + 1):
        print("node {}: ".format(k), end="")
        print("key = {}, ".format(elems[k]), end="")
        if parent_node(k) >= 1:
            print("parent key = {}, ".format(
                elems[parent_node(k)]), end="")
        if left_node(k) <= H:
            print("left key = {}, ".format(
                elems[left_node(k)]), end="")
        if right_node(k) <= H:
            print("right key = {}, ".format(
                elems[right_node(k)]), end="")
        print()


main()
