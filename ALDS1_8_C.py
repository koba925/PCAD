#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin
from random import randrange


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
            if x.parent is None:
                self.root = None
            elif x.parent.left == x:
                x.parent.left = None
            else:
                x.parent.right = None
        elif x.left is None:
            if x.parent is None:
                self.root = x.right
            elif x.parent.left == x:
                x.parent.left = x.right
            else:
                x.parent.right = x.right
            x.right.parent = x.parent
        elif x.right is None:
            if x.parent is None:
                self.root = x.left
            elif x.parent.left == x:
                x.parent.left = x.left
            else:
                x.parent.right = x.left
            x.left.parent = x.parent

    def delete(self, key):
        x = self.find(key)
        if x.left is None or x.right is None:
            self.delete_node(x)
        elif x.right.left is None:
            x.key = x.right.key
            self.delete_node(x.right)
        else:
            y = x.right.leftmost_child()
            x.key = y.key
            self.delete_node(y)

    def fold_inorder(self, f, init):
        def rec(node, b):
            nonlocal f, init

            if not node:
                return b
            else:
                return rec(node.right,
                           f(node.key,
                             rec(node.left, b)))

        return rec(self.root, init)

    def flatten_inorder(self):
        return self.fold_inorder(
            lambda a, b: b + [a],
            [])

    def foreach_inorder(self, f):

        def rec(node):
            if not node:
                return
            else:
                rec(node.left)
                f(node.key)
                rec(node.right)

        rec(self.root)

    def print_inorder(self):
        self.foreach_inorder(
            lambda a: print("", a, end="")
        )
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
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

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


def process(commands):
    T = Tree()
    for cmd in commands:
        if cmd[0] == "insert":
            T.insert(Node(int(cmd[1])))
        elif cmd[0] == "find":
            print("yes" if T.find(int(cmd[1])) else "no")
        elif cmd[0] == "delete":
            T.delete(int(cmd[1]))
        elif cmd[0] == "print":
            T.print_inorder()
            T.print_preorder()
    return T


def main():
    _ = int(stdin.readline())
    commands = []
    for line in stdin:
        commands.append(line.split())
    process(commands)


def random_test_repr(n, p, q, T):
    return "n:{}\np:{}\nq:{}\nT:{}".format(
        n, p, q, str(T))


def test_a_random_case(p, q):
    T = Tree()
    inserted = []

    for n in p:
        assert not T.find(n), \
            "Before Insert:\n" + \
            random_test_repr(n, p, q, str(T))
        T.insert(Node(n))
        assert T.find(n), \
            "After Insert:\n" + \
            random_test_repr(n, p, q, str(T))

        inserted.append(n)
        assert T.flatten_inorder() == sorted(inserted), \
            "Inorder(Inserting):\n" + \
            random_test_repr(n, p, q, str(T))

    for n in q:
        T.delete(n)
        assert not T.find(n), \
            "After Delete:\n" + \
            random_test_repr(n, p, q, str(T))

        inserted.remove(n)
        assert T.flatten_inorder() == sorted(inserted), \
            "Inorder(Deleting):\n" + \
            random_test_repr(n, p, q, str(T))


def random_array(l):
    arr = list(range(l))
    for i in range(l):
        j = randrange(l)
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    return arr


def random_test():
    N = 10000
    L = 7

    for i in range(N):
        test_a_random_case(
            random_array(L), random_array(L))


random_test()
exit()

main()
