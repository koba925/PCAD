#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin
from typing import Any, List, Optional

from enum import IntEnum


class EPStatus(IntEnum):
    BOTTOM = 0
    LEFT = 1
    RIGHT = 2
    TOP = 3


class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "({}, {})".format(self.x, self.y)


class Segment:
    def __init__(
        self, p1: Optional[Point] = None, p2: Optional[Point] = None
    ) -> None:
        self.p1 = Point() if p1 is None else p1
        self.p2 = Point() if p2 is None else p2

    def __repr__(self) -> str:
        return "({}, {})".format(self.p1, self.p2)


class EndPoint:
    def __init__(self, p: Point, seg: Segment, st: EPStatus):
        self.p = p
        self.seg = seg
        self.st = st

    def __lt__(self, other: "EndPoint") -> bool:
        return (
            self.st < other.st
            if self.p.y == other.p.y
            else self.p.y < other.p.y
        )


class Node:
    def __init__(
        self,
        key: Any,
        parent: Optional["Node"] = None,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
    ) -> None:
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return "({} {} {})".format(self.key, self.left, self.right)

    def minimum_child(self) -> "Node":
        x = self
        while x.left is not None:
            x = x.left
        return x

    def successor(self) -> Optional["Node"]:
        if self.right is not None:
            return self.right.minimum_child()

        x = self
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y


class Tree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def __str__(self) -> str:
        return str(self.root) if self.root else "()"

    def insert(self, z: Node) -> None:
        y = None
        x = self.root

        while x is not None:
            y = x
            x = x.left if z.key < x.key else x.right

        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def find(self, key: Any) -> Optional[Node]:
        x = self.root
        while x is not None and key != x.key:
            x = x.left if key < x.key else x.right
        return x

    def delete(self, z: Node) -> None:
        y = z if z.left is None or z.right is None else z.successor()
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

    def lower_bound(self, key: Any) -> Optional[Node]:
        x = self.root
        b: Optional[Node] = None

        while x is not None:
            if key < x.key:
                if b is None or x.key < b.key:
                    b = x
                x = x.left
            elif key == x.key:
                b = x
                break
            else:
                x = x.right

        return b


def manhattanIntersection(S: List[Segment]) -> int:
    def crosses(x1: float, x2: float) -> int:
        cnt: int = 0
        node: Optional[Node] = BT.lower_bound(x1)
        while node is not None and node.key <= x2:
            cnt += 1
            node = node.successor()
        return cnt

    EP: List[EndPoint] = []

    for s in S:
        if (s.p1.y == s.p2.y and s.p1.x > s.p2.x) or (
            s.p1.x == s.p2.x and s.p1.y > s.p2.y
        ):
            s.p1, s.p2 = s.p2, s.p1

        if s.p1.y == s.p2.y:
            EP.append(EndPoint(s.p1, s, EPStatus.LEFT))
            EP.append(EndPoint(s.p2, s, EPStatus.RIGHT))
        else:
            EP.append(EndPoint(s.p1, s, EPStatus.BOTTOM))
            EP.append(EndPoint(s.p2, s, EPStatus.TOP))

    EP.sort()

    BT = Tree()
    cnt = 0

    for e in EP:
        if e.st == EPStatus.TOP:
            BT.delete(BT.find(e.p.x))
        elif e.st == EPStatus.BOTTOM:
            BT.insert(Node(e.p.x))
        elif e.st == EPStatus.LEFT:
            cnt += crosses(e.seg.p1.x, e.seg.p2.x)

    return cnt


def main() -> None:
    S = []

    n = int(stdin.readline())
    for i in range(n):
        x1, y1, x2, y2 = [int(x) for x in stdin.readline().split()]
        S.append(Segment(Point(x1, y1), Point(x2, y2)))

    print(manhattanIntersection(S))


main()
