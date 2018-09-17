#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def print_dict(d):
    print(len(d))
    for i in d:
        print("{} --> {}".format(i, d[i]))


def main():
    d = {"red": 32, "blue": 688, "yellow": 122}
    d["blue"] += 312
    print_dict(d)
    d["zebra"] = 101010
    d["white"] = 0
    del d["yellow"]
    print_dict(d)
    print("{} --> {}".format("red", d["red"]))


main()
