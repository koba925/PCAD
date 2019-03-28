#! /usr/bin/env python3

import unittest
from shape import float_equal, Point, Vector, Segment, Line, Circle, Polygon
from shape import PointLocation as PL
from shape import Containment as CN
import sys

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(3, 5)

    def test_float_equal(self):
        self.assertTrue(float_equal(1, 1))
        self.assertTrue(float_equal(1.00000000001, 1))
        self.assertTrue(float_equal(1, 1.00000000001))
        self.assertFalse(float_equal(1.000000001, 1))
        self.assertFalse(float_equal(1, 1.000000001))

    def test_init_default(self):
        p1 = Point()
        self.assertEqual(p1.x, 0)
        self.assertEqual(p1.y, 0)
        p2 = Point()
        p1.x = 1
        self.assertEqual(p2.x, 0)
        self.assertEqual(p2.y, 0)

    def test_init(self):
        self.assertEqual(self.p1.x, 1)
        self.assertEqual(self.p1.y, 2)

    def test_repr(self):
        self.assertEqual(self.p1.__repr__(), 'Point(1, 2)')

    def test_eq(self):
        self.assertTrue(self.p1 == Point(1, 2))
        self.assertTrue(self.p1 == Point(1.00000000001, 2))
        self.assertTrue(self.p1 == Point(1, 2.00000000001))
        self.assertFalse(self.p1 == Point(1, 3))
        self.assertFalse(self.p1 == Point(2, 2))
        self.assertFalse(self.p1 == Point(2, 3))
        self.assertFalse(self.p1 == 3)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(4, 7))

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Point(-2, -3))

    def test_mul(self):
        self.assertEqual(self.p1 * 2, Point(2, 4))
        self.assertEqual(2 * self.p1, Point(2, 4))

    def test_div(self):
        self.assertEqual(self.p1 / 2, Point(0.5, 1))

    def test_lt(self):
        self.assertTrue(self.p1 < Point(2, 2))
        self.assertFalse(self.p1 < Point(0, 2))
        self.assertTrue(self.p1 < Point(1, 3))
        self.assertTrue(self.p1 < Point(1.00000000001, 3))
        self.assertFalse(self.p1 < Point(1, 1))
        self.assertFalse(self.p1 < Point(1.00000000001, 1))
        self.assertFalse(self.p1 < Point(1, 2))

    def test_norm(self):
        self.assertTrue(Point(3, 4).norm() == 25)
        self.assertTrue(Vector(3, 4).norm() == 25)

    def test_abs(self):
        self.assertTrue(Point(3, 4).abs() == 5)
        self.assertTrue(Vector(3, 4).abs() == 5)

    def test_dot(self):
        self.assertEqual(Point(1, 0).dot(Point(0, 1)), 0)
        self.assertEqual(self.p1.dot(self.p2), 13)

    def test_cross(self):
        self.assertEqual(Point(1, 0).cross(Point(0, 1)), 1)
        self.assertEqual(self.p1.cross(self.p2), -1)

    def test_is_orthogonal(self):
        self.assertTrue(Point(1, 0).is_orthogonal(Point(0, 1)))
        self.assertFalse(Point(0, 1).is_orthogonal(Point(1, 1)))

    def test_is_parallel(self):
        self.assertFalse(Point(1, 0).is_parallel(Point(0, 1)))
        self.assertTrue(Point(0, 1).is_parallel(Point(0, 1)))

    def test_projection(self):
        self.assertEqual(
            Segment(Point(0, 0),
                    Point(4, 0)).projection(Point(2, 2)),
            Point(2, 0))

    def test_distance(self):
        self.assertEqual(
            Point(1, 1).distance(Point(4, 5)),
            5)

    def test_in_side_of(self):
        s1 = Segment(Point(0, 0), Point(0, 1))
        self.assertFalse(Point(2, -1).in_side_of(s1))
        self.assertTrue(Point(2, 0).in_side_of(s1))
        self.assertTrue(Point(2, 1).in_side_of(s1))

    def test_in_width_of(self):
        s1 = Segment(Point(0, -1), Point(0, 1))
        self.assertFalse(Point(2, -2).in_width_of(s1))
        self.assertTrue(Point(2, -1).in_width_of(s1))
        self.assertTrue(Point(2, 0).in_width_of(s1))
        self.assertTrue(Point(2, 1).in_width_of(s1))
        self.assertFalse(Point(2, 2).in_width_of(s1))

        s1 = Segment(Point(-1, 0), Point(1, 0))
        self.assertFalse(Point(5, 3).in_width_of(s1))

    def test_distance_to_line(self):
        s1 = Segment(Point(-1, 0), Point(1, 0))
        self.assertEqual(Point(0, 3).distance_to_line(s1), 3)

    def test_distance_to_segment(self):
        s1 = Segment(Point(-1, 0), Point(1, 0))
        self.assertEqual(Point(-5, 3).distance_to_segment(s1), 5)
        self.assertEqual(Point(0, 3).distance_to_segment(s1), 3)
        self.assertEqual(Point(5, 3).distance_to_segment(s1), 5)


class TestVector(unittest.TestCase):

    def test_init(self):
        v = Vector(1, 2)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)


class TestSegment(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(3, 5)
        self.s = Segment(self.p1, self.p2)

    def test_init_default(self):
        s1 = Segment()
        self.assertEqual(s1.p1, Point(0, 0))
        self.assertEqual(s1.p2, Point(0, 0))
        s2 = Segment()
        s1.p1.x = 1
        self.assertEqual(s2.p1, Point(0, 0))
        self.assertEqual(s2.p2, Point(0, 0))

    def test_init(self):
        self.assertEqual(self.s.p1, Point(1, 2))
        self.assertEqual(self.s.p2, Point(3, 5))

    def test_eq(self):
        self.assertTrue(
            self.s == Segment(Point(1, 2), Point(3, 5)))
        self.assertFalse(
            self.s == Segment(Point(1, 3), Point(3, 5)))
        self.assertFalse(
            self.s == Segment(Point(1, 2), Point(3, 6)))
        self.assertFalse(
            self.s == Segment(Point(1, 3), Point(3, 6)))
        self.assertFalse(self.s == 3)

    def test_repr(self):
        self.assertEqual(self.s.__repr__(),
                         'Segment(Point(1, 2), Point(3, 5))')

    def test_vector(self):
        self.assertEqual(self.s.vector(), Vector(2, 3))

    def test_reverse(self):
        self.assertEqual(self.s.reverse(),
                         Segment(self.p2, self.p1))

    def test_length(self):
        self.assertEqual(Segment(Point(1, 2),
                                 Point(4, 6)).length(),
                         5)

    def test_is_orthogonal(self):
        s1 = Segment(Point(0, 0), Point(1, 0))
        s2 = Segment(Point(0, 0), Point(0, 1))
        self.assertTrue(s1.is_orthogonal(s2))
        self.assertFalse(s1.is_orthogonal(s1))

    def test_is_parallel(self):
        s1 = Segment(Point(0, 0), Point(1, 0))
        s2 = Segment(Point(0, 0), Point(0, 1))
        self.assertTrue(s1.is_parallel(s1))
        self.assertFalse(s1.is_parallel(s2))

    def test_intersects(self):
        p1 = Point(0, 0)
        p2 = Point(4, 0)
        p3 = Point(0, 2)
        p4 = Point(4, 2)
        p5 = Point(2, 0)
        self.assertTrue(
            Segment(p1, p4).intersects(Segment(p2, p3)))
        self.assertFalse(
            Segment(p1, p5).intersects(Segment(p2, p3)))

    def test_intersection(self):
        p1 = Point(0, 0)
        p2 = Point(4, 0)
        p3 = Point(0, 2)
        p4 = Point(4, 2)
        p5 = Point(2, 1)
        self.assertEqual(
            Segment(p1, p4).intersection(Segment(p2, p3)),
            p5)

    def test_distance_with_segment(self):
        s = Segment(Point(-1, 0), Point(1, 0))
        t = Segment(Point(0, -1), Point(0, 1))
        self.assertEqual(s.distance_with_segment(t), 0)
        t = Segment(Point(-1, 1), Point(1, 1))
        self.assertEqual(s.distance_with_segment(t), 1)
        t = Segment(Point(-2, 0), Point(0, 0))
        self.assertEqual(s.distance_with_segment(t), 0)
        t = Segment(Point(0, 1), Point(2, 3))
        self.assertEqual(s.distance_with_segment(t), 1)
        t = Segment(Point(5, 3), Point(5, 4))
        self.assertEqual(s.distance_with_segment(t), 5)

    def test_location(self):
        s1 = Segment(Point(1, 2), Point(3, 5))
        self.assertEqual(Point(-1, -1).location(s1),
                         PL.ONLINE_BACK)
        self.assertEqual(Point(2, 3.5).location(s1),
                         PL.ON_SEGMENT)
        self.assertEqual(Point(5, 8).location(s1),
                         PL.ONLINE_FRONT)
        self.assertEqual(Point(3, 6).location(s1),
                         PL.COUNTER_CLOCKWISE)
        self.assertEqual(Point(3, 1).location(s1),
                         PL.CLOCKWISE)
        s2 = Segment(Point(0, 0), Point(0, 2))
        self.assertEqual(Point(0, -1).location(s2),
                         PL.ONLINE_BACK)
        self.assertEqual(Point(0, 1).location(s2),
                         PL.ON_SEGMENT)
        self.assertEqual(Point(0, 3).location(s2),
                         PL.ONLINE_FRONT)
        self.assertEqual(Point(-1, 0).location(s2),
                         PL.COUNTER_CLOCKWISE)
        self.assertEqual(Point(1, 0).location(s2),
                         PL.CLOCKWISE)


class TestLine(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(3, 5)
        self.l = Segment(self.p1, self.p2)

    def test_init(self):
        self.assertEqual(self.l.p1, Point(1, 2))
        self.assertEqual(self.l.p2, Point(3, 5))


class TestCircle(unittest.TestCase):

    def test_init_default(self):
        c = Circle(Point(1, 2), 3)
        self.assertEqual(c.c, Point(1, 2))
        self.assertEqual(c.r, 3)

    def test_init(self):
        c = Circle(Point(1, 2), 3)
        self.assertEqual(c.c, Point(1, 2))
        self.assertEqual(c.r, 3)

    def test_eq(self):
        self.assertTrue(Circle(1, 2) == Circle(1, 2))
        self.assertFalse(Circle(1, 2) == Circle(1, 3))
        self.assertFalse(Circle(1, 2) == Circle(2, 2))
        self.assertFalse(Circle(1, 2) == Circle(2, 3))
        self.assertFalse(Circle(1, 2) == 3)

    def test_repr(self):
        c = Circle(1, 2)
        self.assertEqual(c.__repr__(), 'Circle(1, 2)')

    def test_cross_point_line(self):
        self.assertEqual(
            Circle(Point(2, 3), 2).cross_point_line(
                Line(Point(0, 3), Point(1, 3))),
            [Point(0, 3), Point(4, 3)])
        self.assertEqual(
            Circle(Point(2, 3), 2).cross_point_line(
                Line(Point(4, 0), Point(4, 6))),
            [Point(4, 3), Point(4, 3)])

    def test_cross_point_circle(self):
        self.assertTrue(
            Circle(Point(0, 0), 2).cross_point_circle(
                Circle(Point(2, 0), 2)) ==
            [Point(1.0, -1.7320508075),
             Point(1.0, 1.7320508075)])
        self.assertTrue(
            Circle(Point(0, 0), 2).cross_point_circle(
                Circle(Point(0, 3), 1)) ==
            [Point(0, 2), Point(0, 2)])


class TestPolygon(unittest.TestCase):
    def test_init(self):
        p = Polygon([Point(0, 0), Point(1, 0), Point(0, 1)])
        self.assertEqual(p.vertices, [Point(0, 0), Point(1, 0), Point(0, 1)])
        self.assertEqual(p.n, 3)

    def test_sides(self):
        p = Polygon([Point(0, 0), Point(1, 0), Point(0, 1)])
        self.assertEqual(
            list(p.sides()),
            [Segment(Point(0, 0), Point(1, 0)),
             Segment(Point(1, 0), Point(0, 1)),
             Segment(Point(0, 1), Point(0, 0))])

    def test_contains(self):
        p = Polygon([Point(1, 1),
                     Point(7, 1),
                     Point(7, 3),
                     Point(5, 5),
                     Point(5, 3),
                     Point(3, 3),
                     Point(1, 5)])
        self.assertEqual(p.contains(Point(0, 0)), CN.OUTSIDE)
        self.assertEqual(p.contains(Point(0, 1)), CN.OUTSIDE)
        self.assertEqual(p.contains(Point(1, 1)), CN.ONLINE)
        self.assertEqual(p.contains(Point(4, 1)), CN.ONLINE)
        self.assertEqual(p.contains(Point(7, 1)), CN.ONLINE)
        self.assertEqual(p.contains(Point(0, 2)), CN.OUTSIDE)
        self.assertEqual(p.contains(Point(1, 2)), CN.ONLINE)
        self.assertEqual(p.contains(Point(4, 2)), CN.INSIDE)
        self.assertEqual(p.contains(Point(7, 2)), CN.ONLINE)
        self.assertEqual(p.contains(Point(0, 3)), CN.OUTSIDE)
        self.assertEqual(p.contains(Point(1, 3)), CN.ONLINE)
        self.assertEqual(p.contains(Point(2, 3)), CN.INSIDE)
        self.assertEqual(p.contains(Point(3, 3)), CN.ONLINE)
        self.assertEqual(p.contains(Point(4, 3)), CN.ONLINE)
        self.assertEqual(p.contains(Point(5, 3)), CN.ONLINE)
        self.assertEqual(p.contains(Point(6, 3)), CN.INSIDE)
        self.assertEqual(p.contains(Point(7, 3)), CN.ONLINE)
        self.assertEqual(p.contains(Point(0, 4)), CN.OUTSIDE)
        self.assertEqual(p.contains(Point(1, 4)), CN.ONLINE)
        self.assertEqual(p.contains(Point(2, 4)), CN.ONLINE)
        self.assertEqual(p.contains(Point(4, 4)), CN.OUTSIDE)
        self.assertEqual(p.contains(Point(5, 4)), CN.ONLINE)
        self.assertEqual(p.contains(Point(6, 4)), CN.ONLINE)
        self.assertEqual(p.contains(Point(0, 5)), CN.OUTSIDE)
        self.assertEqual(p.contains(Point(1, 5)), CN.ONLINE)
        self.assertEqual(p.contains(Point(4, 5)), CN.OUTSIDE)
        self.assertEqual(p.contains(Point(5, 5)), CN.ONLINE)

        p = Polygon([Point(1, 1),
                     Point(7, 1),
                     Point(5, 3),
                     Point(3, 3),
                     Point(1, 5)])
        self.assertEqual(p.contains(Point(2, 3)), CN.INSIDE)


if __name__ == "__main__":
    unittest.main()
