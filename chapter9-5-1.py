#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def print_set(s):
    print("{}:".format(len(s)), end="")
    for i in s:
        print(" {}".format(i), end="")
    print()


def main():
    s = set([8, 1, 7, 4, 8, 4])
    print_set(s)
    s.discard(7)
    print_set(s)
    s.add(2)
    print_set(s)
    if 10 not in s:
        print("not found.")


main()
