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

    def is_online(self):
        return self in [PointLocation.ON_SEGMENT,
                        PointLocation.ONLINE_BACK,
                        PointLocation.ONLINE_FRONT]


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

    def __str__(self) -> str:
        return f"{self.x} {self.y}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
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

    def my_contains(self, p: Point) -> Containment:
        ps = Segment(p, Point(100000.0, p.y))
        count = 0

        prev_l = self.vertices[0].location(ps)
        if prev_l.is_online():
            prev_l = self.vertices[-1].location(ps)

        for s in self.sides():
            if p.location(s) == PointLocation.ON_SEGMENT:
                return Containment.ONLINE
            cur_l = s.p2.location(ps)
            if cur_l.is_online() or prev_l == cur_l:
                continue
            if ps.intersects(s):
                count += 1
            prev_l = cur_l

        return Containment.OUTSIDE if count % 2 == 0 \
            else Containment.INSIDE

    def contains(self, p: Point) -> Containment:
        ps = Segment(p, Point(100000.0, p.y))
        count = 0

        for s in self.sides():
            if p.location(s) == PointLocation.ON_SEGMENT:
                return Containment.ONLINE
            if s.p1.y > s.p2.y:
                s = s.reverse()
            l1 = s.p1.location(ps)
            l2 = s.p2.location(ps)
            if l1 != PointLocation.COUNTER_CLOCKWISE and \
                l2 == PointLocation.COUNTER_CLOCKWISE and \
                ps.intersects(s):
                count += 1

        return Containment.OUTSIDE if count % 2 == 0 \
            else Containment.INSIDE

    def text_contains(self, p: Point) -> Containment:
        x = False
        for s in self.sides():
            a = s.p1 - p
            b = s.p2 - p
            # print(a, b, a.cross(b), a.dot(b))
            if abs(a.cross(b)) < EPS and a.dot(b) < EPS:
                return Containment.ONLINE
            if a.y > b.y:
                tmp = a
                a = b
                b = tmp
            # print(a, b, a.cross(b))
            if a.y < EPS < b.y and a.cross(b) > EPS:
                x = not x
            # print(x)
        return Containment.INSIDE if x else Containment.OUTSIDE

"""
p = Polygon([Point(0,0),Point(3,1),Point(3,3),Point(0,3)])
print(p.contains(Point(1,1)))
"""