#! /usr/local/bin/python3
# coding: utf-8


class Node():
    def __init__(self, parent=-1, child=[]):
        self.parent = parent
        self.child = child


def node_depth(u, id):
    if u[id].parent == -1:
        return 0
    else:
        return node_depth(u, u[id].parent) + 1


def node_type(u, id):
    if u[id].parent == -1:
        return "root"
    elif u[id].child == []:
        return "leaf"
    else:
        return "internal node"


def main():
    n = int(input())
    u = [Node() for _ in range(n)]

    for _ in range(n):
        id, _, *child = (int(x) for x in input().split())
        u[id].child = child
        for c in child:
            u[c].parent = id

    for id in range(n):
        print("node {}: parent = {}, depth = {}, {}, {}".
              format(id, u[id].parent,
                     node_depth(u, id), node_type(u, id),
                     u[id].child))


main()
