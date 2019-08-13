#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

# from shape import Point, Segment

class Point:
    def __init__(self, x: float=0.0, y: float=0.0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "({}, {})".format(self.x, self.y)

class Segment:
    def __init__(self, p1=None, p2=None):
        self.p1=Point() if p1 is None else p1
        self.p2=Point() if p2 is None else p2

    def __repr__(self) -> str:
        return "({}, {})".format(self.p1, self.p2)

class Node():
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return "({} {} {})".format(
            self.key, self.left, self.right)

    def minimum_child(self):
        x = self
        while x.left is not None:
            x = x.left
        return x

    def maximum_child(self):
        x = self
        while x.right is not None:
            x = x.right
        return x

    def successor(self):
        if self.right is not None:
            return self.right.minimum_child()

        x = self
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y


class Tree():
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root) if self.root else "()"

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
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def delete(self, z):
        # print(self,z)
        y = z if z.left is None or z.right is None \
            else z.successor()
        x = y.right if y.left is None else y.left

        if x is not None:
            x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        if y != z:
            z.key = y.key


def crosses(x1, x2, T):
    node = T.root
    leftmost = None
        
    # print("in crosses:", x1, x2)

    while node is not None:
        # print("crosses node leftmost", node, leftmost)
        if x1 < node.key[1].p1.x:
            if leftmost is None or node.key[1].p1.x < leftmost.key[1].p1.x:
                leftmost = node
            node = node.left
        elif x1 == node.key[1].p1.x:
            leftmost = node
            break
        else:
            node = node.right

    # print("crosses leftmost:", leftmost)
    
    if leftmost is None:
        return 0

    n_crosses = 0
    node = leftmost
    while node is not None and node.key[1].p2.x <= x2:
        n_crosses += 1
        node = node.successor()

    # print(n_crosses)
    return n_crosses

def main():
    n = int(stdin.readline())
    segments = []

    for i in range(n):
        x1, y1, x2, y2 = [int(x) for x in stdin.readline().split()]
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
        else:
            if x1 > x2:
                x1, x2 = x2, x1
        seg = Segment(Point(x1, y1), Point(x2, y2))
        if x1 == x2:
            segments.append((y1, 1, seg))
            segments.append((y2, 3, seg))
        else:
            segments.append((y1, 2, seg))

    segments.sort(key=lambda elem: (elem[0], elem[1]))
    # print(*segments, sep="\n")

    T = Tree()
    n_cross = 0

    for y, k, seg in segments:
        # print(y, k, seg)
        if k == 1:
            T.insert(Node((seg.p1.x, seg)))
        elif k == 3:
            T.delete(T.find((seg.p1.x, seg)))
        else:
            n_cross += crosses(seg.p1.x, seg.p2.x, T)
        # print(T)

    print(n_cross)

main()
