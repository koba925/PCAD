#! /usr/local/bin/python3
# coding: utf-8


class Node():
    NIL = -1

    def __init__(self, parent=NIL, left=NIL, right=NIL, depth=-1):
        self.parent = parent
        self.left = left
        self.right = right
        self.depth = depth


def read_nodes(T):
    for _ in range(len(T)):
        id, _, *child = [int(x) for x in input().split()]
        for i, c in enumerate(child):
            if i == 0:
                T[id].left = c
            else:
                T[l].right = c
            l = c
            T[c].parent = id


def calc_depth(T):

    def rec(r, p):
        nonlocal T

        T[r].depth = p
        if T[r].right != Node.NIL:
            rec(T[r].right, p)
        if T[r].left != Node.NIL:
            rec(T[r].left, p + 1)

    rec([u.parent for u in T].index(-1), 0)


def node_type(T, id):
    if T[id].parent == Node.NIL:
        return "root"
    elif T[id].left == Node.NIL:
        return "leaf"
    else:
        return "internal node"


def child(T, id):
    c = []
    i = T[id].left
    while i != Node.NIL:
        c.append(i)
        i = T[i].right
    return c


def print_nodes(T):
    for id in range(len(T)):
        print("node {}: parent = {}, depth = {}, {}, {}".
              format(id, T[id].parent, T[id].depth,
                     node_type(T, id), child(T, id)))


def main():
    n = int(input())
    T = [Node() for _ in range(n)]

    read_nodes(T)
    calc_depth(T)
    print_nodes(T)


main()
