#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin


class Node():
    NIL = -1

    def __init__(self, p=NIL, l=NIL, r=NIL, d=-1, h=-1):
        self.p = p
        self.l = l
        self.r = r
        self.d = d
        self.h = h

    def __repr__(self):
        return "Node({}, {}, {}, {})".format(self.p, self.l, self.r, self.d)


def root_of(T):
    return [u.p for u in T].index(Node.NIL)


def sibling_of(T, id):
    if T[id].p == Node.NIL:
        return Node.NIL
    p = T[T[id].p]
    if p.l == id:
        return p.r
    if p.r == id:
        return p.l
    return Node.NIL


def degree_of(T, id):
    l = 0 if T[id].l == Node.NIL else 1
    r = 0 if T[id].r == Node.NIL else 1
    return l + r


def calc_depth(T):

    def rec(id, depth):
        nonlocal T

        T[id].d = depth
        if T[id].l != Node.NIL:
            rec(T[id].l, depth + 1)
        if T[id].r != Node.NIL:
            rec(T[id].r, depth + 1)

    rec(root_of(T), 0)


def calc_height(T):

    def rec(id):
        nonlocal T

        l = 0 if T[id].l == Node.NIL else rec(T[id].l) + 1
        r = 0 if T[id].r == Node.NIL else rec(T[id].r) + 1
        T[id].h = max(l, r)
        return T[id].h

    rec(root_of(T))


def type_of(T, id):
    if T[id].p == Node.NIL:
        return "root"
    elif T[id].l == Node.NIL and T[id].r == Node.NIL:
        return "leaf"
    else:
        return "internal node"


def read_nodes(T):
    for line in stdin:
        id, l, r = [int(x) for x in line.split()]
        T[id].l = l
        if l != Node.NIL:
            T[l].p = id
        T[id].r = r
        if r != Node.NIL:
            T[r].p = id


def print_nodes(T):
    for id in range(len(T)):
        print("node {}: ".format(id), end="")
        print("parent = {}, ".format(T[id].p), end="")
        print("sibling = {}, ".format(sibling_of(T, id)), end="")
        print("degree = {}, ".format(degree_of(T, id)), end="")
        print("depth = {}, ".format(T[id].d), end="")
        print("height = {}, ".format(T[id].h), end="")
        print(type_of(T, id))


def main():
    n = int(stdin.readline())
    T = [Node() for _ in range(n)]

    read_nodes(T)
    calc_depth(T)
    calc_height(T)
    print_nodes(T)


main()
