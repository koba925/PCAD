#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin


class Tree():
    def __init__(self):
        self.root = None

    def insert(self, z):

        def rec(node):
            nonlocal z

            if node is None:
                return z
            elif z.key < node.key:
                return Node(node.key,
                            rec(node.left),
                            node.right)
            else:
                return Node(node.key,
                            node.left,
                            rec(node.right))

        self.root = rec(self.root)
        print(self.root)

    def print_inorder(self):
        def rec(node):
            if not node:
                return
            else:
                rec(node.left)
                print("", node.key, end="")
                rec(node.right)

        rec(self.root)
        print()

    def print_preorder(self):

        def rec(node):
            if not node:
                return
            else:
                print("", node.key, end="")
                rec(node.left)
                rec(node.right)

        rec(self.root)
        print()


class Node():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node({}, {}, {})".format(
            self.key, self.left, self.right)


def main():
    _ = int(stdin.readline())
    T = Tree()

    for line in stdin:
        cmd, *args = line.split()
        if cmd == "insert":
            T.insert(Node(int(args[0])))
        elif cmd == "print":
            T.print_inorder()
            T.print_preorder()


main()
