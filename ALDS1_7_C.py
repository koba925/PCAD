#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin


class Node():
    NIL = -1

    def __init__(self):
        self.parent = Node.NIL
        self.left = Node.NIL
        self.right = Node.NIL


def read_nodes(T):
    for line in stdin:
        id, left, right = [int(x) for x in line.split()]
        T[id].left = left
        if left != Node.NIL:
            T[left].parent = id
        T[id].right = right
        if right != Node.NIL:
            T[right].parent = id


def root_of(T):
    return [u.parent for u in T].index(Node.NIL)


def walk_preorder(T):

    def rec(id):
        nonlocal T

        if id == Node.NIL:
            return
        print("", id, end="")
        rec(T[id].left)
        rec(T[id].right)

    print("Preorder")
    rec(root_of(T))
    print()


def walk_inorder(T):

    def rec(id):
        nonlocal T

        if id == Node.NIL:
            return
        rec(T[id].left)
        print("", id, end="")
        rec(T[id].right)

    print("Inorder")
    rec(root_of(T))
    print()


def walk_postorder(T):

    def rec(id):
        nonlocal T

        if id == Node.NIL:
            return
        rec(T[id].left)
        rec(T[id].right)
        print("", id, end="")

    print("Postorder")
    rec(root_of(T))
    print()


def main():
    n = int(stdin.readline())
    T = [Node() for _ in range(n)]

    read_nodes(T)
    walk_preorder(T)
    walk_inorder(T)
    walk_postorder(T)


main()
