#! /usr/bin/env python3

from typing import List, Tuple, Optional, Generator
from math import sqrt, sin, cos, acos, atan2
from enum import IntEnum

EPS = 1e-10


def float_equal(x: float, y: float) -> bool:
    return abs(x - y) < EPS


class PointLocation(IntEnum):
    COUNTER_CLOCKWISE = 1
    CLOCKWISE = -1
    ONLINE_BACK = 2
    ONLINE_FRONT = -2
    ON_SEGMENT = 0


class Containment(IntEnum):
    OUTSIDE = 0
    ONLINE = 1
    INSIDE = 2


class Point:

    def __init__(self, x: float=0.0, y: float=0.0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            # print("NotImplemented in Point")
            return NotImplemented
        return float_equal(self.x, other.x) and \
            float_equal(self.y, other.y)

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, k: float) -> 'Point':
        return Point(self.x * k, self.y * k)

    def __rmul__(self, k: float) -> 'Point':
        return self * k

    def __truediv__(self, k: float) -> 'Point':
        return Point(self.x / k, self.y / k)

    def __lt__(self, other: 'Point') -> bool:
        return self.y < other.y \
            if abs(self.x - other.x) < EPS \
            else self.x < other.x

    @staticmethod
    def polar(a: float, r: float) -> 'Point':
        return Point(a * cos(r), a * sin(r))

    def arg(self) -> float:
        return atan2(self.y, self.x)

    def norm(self) -> float:
        return self.x * self.x + self.y * self.y

    def abs(self) -> float:
        return sqrt(self.norm())

    def dot(self, other: 'Point') -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other: 'Point') -> float:
        return self.x * other.y - self.y * other.x

    def is_orthogonal(self, other: 'Point') -> bool:
        return float_equal(self.dot(other), 0.0)

    def is_parallel(self, other: 'Point') -> bool:
        return float_equal(self.cross(other), 0.0)

    def distance(self, other: 'Point') -> float:
        return (self - other).abs()

    def in_side_of(self, seg: 'Segment') -> bool:
        return seg.vector().dot(
            Segment(seg.p1, self).vector()) >= 0

    def in_width_of(self, seg: 'Segment') -> bool:
        return \
            self.in_side_of(seg) and \
            self.in_side_of(seg.reverse())

    def distance_to_line(self, seg: 'Segment') -> float:
        return \
            abs((self - seg.p1).cross(seg.vector())) / \
            seg.length()

    def distance_to_segment(self, seg: 'Segment') -> float:
        if not self.in_side_of(seg):
            return self.distance(seg.p1)
        if not self.in_side_of(seg.reverse()):
            return self.distance(seg.p2)
        else:
            return self.distance_to_line(seg)

    def location(self, seg: 'Segment') -> PointLocation:
        p = self - seg.p1
        d = seg.vector().cross(p)
        if d > EPS:
            return PointLocation.COUNTER_CLOCKWISE
        if d < -EPS:
            return PointLocation.CLOCKWISE
        if seg.vector().dot(p) < 0.0:
            return PointLocation.ONLINE_BACK
        if seg.vector().norm() < p.norm():
            return PointLocation.ONLINE_FRONT
        return PointLocation.ON_SEGMENT


Vector = Point


class Segment:

    def __init__(self,
                 p1: Optional[Point] = None,
                 p2: Optional[Point] = None) -> None:
        self.p1: Point = Point() if p1 is None else p1
        self.p2: Point = Point() if p2 is None else p2

    def __repr__(self) -> str:
        return "Segment({}, {})".format(self.p1, self.p2)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Segment):
            # print("NotImplemented in Segment")
            return NotImplemented
        return self.p1 == other.p1 and self.p2 == other.p2

    def vector(self) -> Vector:
        return self.p2 - self.p1

    def reverse(self) -> 'Segment':
        return Segment(self.p2, self.p1)

    def length(self) -> float:
        return self.p1.distance(self.p2)

    def is_orthogonal(self, other: 'Segment') -> bool:
        return self.vector().is_orthogonal(other.vector())

    def is_parallel(self, other: 'Segment') -> bool:
        return self.vector().is_parallel(other.vector())

    def projection(self, p: Point) -> Point:
        v = self.vector()
        vp = p - self.p1
        return v.dot(vp) / v.norm() * v + self.p1

    def reflection(self, p: Point) -> Point:
        x = self.projection(p)
        return p + 2 * (x - p)

    def intersects(self, other: 'Segment') -> bool:
        d0: PointLocation = self.p1.location(other)
        d1: PointLocation = self.p2.location(other)
        d2: PointLocation = other.p1.location(self)
        d3: PointLocation = other.p2.location(self)
        return d0 * d1 * d2 * d3 == 0 or \
            (d0 * d1 == -1 and d2 * d3 == -1)

    def intersection(self, other: 'Segment') -> Point:
        a = self.vector()
        b = other.vector()
        c = self.p1 - other.p1
        s = b.cross(c) / a.cross(b)
        return self.p1 + s * a

    def distance_with_segment(self, other: 'Segment') -> float:
        if not self.is_parallel(other) and \
                self.intersects(other):
            return 0
        else:
            return min(
                self.p1.distance_to_segment(other),
                self.p2.distance_to_segment(other),
                other.p1.distance_to_segment(self),
                other.p2.distance_to_segment(self))


Line = Segment


class Circle:

    def __init__(self,
                 c: Optional[Point] = None,
                 r: float=0.0) -> None:
        self.c: Point = Point() if c is None else c
        self.r: float = r

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.c == other.c and self.r == other.r

    def __repr__(self) -> str:
        return "Circle({}, {})".format(self.c, self.r)

    def cross_point_line(self, line: Line) -> List[Point]:
        proj = line.projection(self.c)
        dist = self.c.distance_to_line(line)
        tan = sqrt(self.r * self.r - dist * dist)
        u = line.vector() / line.vector().abs()
        return sorted([proj - tan * u, proj + tan * u])

    def cross_point_circle(self, other: 'Circle') -> List[Point]:
        d = (other.c - self.c).abs()
        r1 = self.r
        r2 = other.r
        a = acos((r1 * r1 + d * d - r2 * r2) / (2 * r1 * d))
        t = (other.c - self.c).arg()
        return sorted([self.c + Vector.polar(self.r, t + a),
                       self.c + Vector.polar(self.r, t - a)])


class Polygon:
    def __init__(self, vertices: List[Point]) -> None:
        self.vertices = vertices
        self.n = len(vertices)

    def sides(self) -> Generator[Segment, None, None]:
        for i in range(self.n):
            yield Segment(self.vertices[i],
                          self.vertices[(i + 1) % self.n])

    def next(self, k: int) -> int:
        return (k + 1) % self.n

    def contains(self, p: Point) -> Containment:
        ps = Segment(p, Point(100000.0, p.y))
        count = 0
        for k in range(self.n):
            p1 = self.vertices[k]
            k = self.next(k)
            p2 = self.vertices[k]
            s = Segment(p1, p2)
            if p.location(s) == PointLocation.ON_SEGMENT:
                return Containment.ONLINE
            if p.x < p1.x and float_equal(p.y, p1.y):
                continue
            if p.x < p2.x and float_equal(p.y, p2.y):
                k = self.next(k)
                while True:
                    p3 = self.vertices[k]
                    if not float_equal(p2.y, p3.y):
                        break
                    k = self.next(k)
                if p1.y < p2.y < p3.y or p1.y > p2.y > p3.y:
                    count += 1
            elif ps.intersects(s):
                count += 1
        return Containment.OUTSIDE if count % 2 == 0 \
            else Containment.INSIDE
