#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin
from functools import reduce


class Node():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node({}, {}, {})".format(
            self.key, self.left, self.right)


def insert(tree, z):
    if tree is None:
        return z
    elif z.key < tree.key:
        return Node(tree.key,
                    insert(tree.left, z),
                    tree.right)
    else:
        return Node(tree.key,
                    tree.left,
                    insert(tree.right, z))


def flatten_inorder(tree):
    if tree is None:
        return []
    else:
        return flatten_inorder(tree.left) + \
            [tree.key] + \
            flatten_inorder(tree.right)


def flatten_preorder(tree):
    if tree is None:
        return []
    else:
        return [tree.key] + \
            flatten_preorder(tree.left) + \
            flatten_preorder(tree.right)


def process(tree, command):
    if command[0] == "insert":
        return insert(tree, Node(int(command[1])))
    elif command[0] == "print":
        print("", *flatten_inorder(tree))
        print("", *flatten_preorder(tree))
        return tree


def main():
    _ = int(stdin.readline())

    reduce(process,
           [line.split() for line in stdin],
           None)


main()
