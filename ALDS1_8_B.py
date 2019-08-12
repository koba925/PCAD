#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin


class Tree():
    def __init__(self):
        self.root = None

    def insert(self, z):

        y = None
        x = self.root

        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def find(self, key):
        x = self.root
        while x != None:
            if key == x.key:
                return True
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return False

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
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


def main():
    _ = int(stdin.readline())
    T = Tree()

    for line in stdin:
        cmd, *args = line.split()
        if cmd == "insert":
            T.insert(Node(int(args[0])))
        if cmd == "find":
            print("yes" if T.find(int(args[0])) else "no")
        elif cmd == "print":
            T.print_inorder()
            T.print_preorder()


main()
