#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin


class Tree():
    def __init__(self):
        self.root = None

    def insert(self, z):

        y = None
        x = self.root

        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def find(self, key):
        x = self.root
        while x is not None:
            if key == x.key:
                return x
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return None

    def delete_node(self, x):
        if x.left is None and x.right is None:
            if x.parent.left == x:
                x.parent.left = None
            else:
                x.parent.right = None
        elif x.left is None:
            if x.parent.left == x:
                x.parent.left = x.right
            else:
                x.parent.right = x.right
            x.right.parent = x.parent
        elif x.right is None:
            if x.parent.left == x:
                x.parent.left = x.left
            else:
                x.parent.right = x.left
            x.left.parent = x.parent

    def delete(self, key):
        x = self.find(key)
        if x.left is None or x.right is None:
            delete_node(self, x)
        elif x.left.right is None:
            x.left.parent = x.parent
            if x.parent.left == x:
                x.parent.left = x.left
            else:
                x.parent.right = x.left
            x.left.right = x.right
            x.right.parent = x.left
        else:
            y = x.left.rightmost_child()
            z = y.leftmost_child()
            # print("y {}, z {}".format(y.key, z.key))

            y.parent.right = None

            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
            y.parent = x.parent

            x.right.parent = y
            y.right = x.right

            x.left.parent = z
            z.left = x.left

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

    def __str__(self):
        return str(self.root) if self.root else "()"


class Node():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def rightmost_child(self):
        x = self
        while x.right is not None:
            x = x.right
        return x

    def leftmost_child(self):
        x = self
        while x.left is not None:
            x = x.left
        return x

    def __str__(self):
        return "({} {} {})".format(
            self.key, self.left, self.right)


def main():
    _ = int(stdin.readline())
    T = Tree()

    for line in stdin:
        cmd, *args = line.split()
        if cmd == "insert":
            T.insert(Node(int(args[0])))
        elif cmd == "find":
            print("yes" if T.find(int(args[0])) else "no")
        elif cmd == "delete":
            T.delete(int(args[0]))
        elif cmd == "print":
            T.print_inorder()
            T.print_preorder()
        print(T)


main()
