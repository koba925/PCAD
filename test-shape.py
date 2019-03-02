#! /usr/bin/env python3

import unittest
from shape import float_equal, Point, Vector, Segment, Line, Circle


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1.0, 2.0)
        self.p2 = Point(3.0, 5.0)

    def test_float_equal(self):
        self.assertTrue(float_equal(1.0, 1.0))
        self.assertTrue(float_equal(1.00000000001, 1.0))
        self.assertTrue(float_equal(1.0, 1.00000000001))
        self.assertFalse(float_equal(1.000000001, 1.0))
        self.assertFalse(float_equal(1.0, 1.000000001))

    def test_init_default(self):
        p1 = Point()
        self.assertEqual(p1.x, 0.0)
        self.assertEqual(p1.y, 0.0)
        p2 = Point()
        p1.x = 1.0
        self.assertEqual(p2.x, 0.0)
        self.assertEqual(p2.y, 0.0)

    def test_init(self):
        self.assertEqual(self.p1.x, 1.0)
        self.assertEqual(self.p1.y, 2.0)

    def test_repr(self):
        self.assertEqual(self.p1.__repr__(), 'Point(1.0, 2.0)')

    def test_eq(self):
        self.assertTrue(self.p1 == Point(1.0, 2.0))
        self.assertTrue(self.p1 == Point(1.00000000001, 2.0))
        self.assertTrue(self.p1 == Point(1.0, 2.00000000001))
        self.assertFalse(self.p1 == Point(1.0, 3.0))
        self.assertFalse(self.p1 == Point(2.0, 2.0))
        self.assertFalse(self.p1 == Point(2.0, 3.0))
        self.assertFalse(self.p1 == 3)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(4.0, 7.0))

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Point(-2.0, -3.0))

    def test_mul(self):
        self.assertEqual(self.p1 * 2, Point(2.0, 4.0))
        self.assertEqual(2 * self.p1, Point(2.0, 4.0))

    def test_div(self):
        self.assertEqual(self.p1 / 2.0, Point(0.5, 1.0))

    def test_lt(self):
        self.assertTrue(self.p1 < Point(2.0, 2.0))
        self.assertFalse(self.p1 < Point(0.0, 2.0))
        self.assertTrue(self.p1 < Point(1.0, 3.0))
        self.assertTrue(self.p1 < Point(1.00000000001, 3.0))
        self.assertFalse(self.p1 < Point(1.0, 1.0))
        self.assertFalse(self.p1 < Point(1.00000000001, 1.0))
        self.assertFalse(self.p1 < Point(1.0, 2.0))

    def test_norm(self):
        self.assertTrue(Point(3.0, 4.0).norm() == 25.0)
        self.assertTrue(Vector(3.0, 4.0).norm() == 25.0)

    def test_abs(self):
        self.assertTrue(Point(3.0, 4.0).abs() == 5.0)
        self.assertTrue(Vector(3.0, 4.0).abs() == 5.0)

    def test_dot(self):
        self.assertEqual(Point(1.0, 0.0).dot(Point(0.0, 1.0)), 0.0)
        self.assertEqual(self.p1.dot(self.p2), 13.0)

    def test_cross(self):
        self.assertEqual(Point(1.0, 0.0).cross(Point(0.0, 1.0)), 1.0)
        self.assertEqual(self.p1.cross(self.p2), -1.0)

    def test_is_orthogonal(self):
        self.assertTrue(Point(1.0, 0.0).is_orthogonal(Point(0.0, 1.0)))
        self.assertFalse(Point(0.0, 1.0).is_orthogonal(Point(1.0, 1.0)))

    def test_is_parallel(self):
        self.assertFalse(Point(1.0, 0.0).is_parallel(Point(0.0, 1.0)))
        self.assertTrue(Point(0.0, 1.0).is_parallel(Point(0.0, 1.0)))

    def test_distance(self):
        self.assertEqual(
            Point(1.0, 1.0).distance(Point(4.0, 5.0)),
            5.0)

    def test_in_side_of(self):
        s1 = Segment(Point(0.0, 0.0), Point(0.0, 1.0))
        self.assertFalse(Point(2.0, -1.0).in_side_of(s1))
        self.assertTrue(Point(2.0, 0.0).in_side_of(s1))
        self.assertTrue(Point(2.0, 1.0).in_side_of(s1))

    def test_in_width_of(self):
        s1 = Segment(Point(0.0, -1.0), Point(0.0, 1.0))
        self.assertFalse(Point(2.0, -2.0).in_width_of(s1))
        self.assertTrue(Point(2.0, -1.0).in_width_of(s1))
        self.assertTrue(Point(2.0, 0.0).in_width_of(s1))
        self.assertTrue(Point(2.0, 1.0).in_width_of(s1))
        self.assertFalse(Point(2.0, 2.0).in_width_of(s1))

        s1 = Segment(Point(-1.0, 0.0), Point(1.0, 0.0))
        self.assertFalse(Point(5.0, 3.0).in_width_of(s1))

    def test_distance_to_line(self):
        s1 = Segment(Point(-1.0, 0.0), Point(1.0, 0.0))
        self.assertEqual(Point(0.0, 3.0).distance_to_line(s1), 3.0)

    def test_distance_to_segment(self):
        s1 = Segment(Point(-1.0, 0.0), Point(1.0, 0.0))
        self.assertEqual(Point(-5.0, 3.0).distance_to_segment(s1), 5.0)
        self.assertEqual(Point(0.0, 3.0).distance_to_segment(s1), 3.0)
        self.assertEqual(Point(5.0, 3.0).distance_to_segment(s1), 5.0)


class TestVector(unittest.TestCase):

    def test_init(self):
        v = Vector(1.0, 2.0)
        self.assertEqual(v.x, 1.0)
        self.assertEqual(v.y, 2.0)


class TestSegment(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1.0, 2.0)
        self.p2 = Point(3.0, 5.0)
        self.s = Segment(self.p1, self.p2)

    def test_init_default(self):
        s1 = Segment()
        self.assertEqual(s1.p1, Point(0.0, 0.0))
        self.assertEqual(s1.p2, Point(0.0, 0.0))
        s2 = Segment()
        s1.p1.x = 1.0
        self.assertEqual(s2.p1, Point(0.0, 0.0))
        self.assertEqual(s2.p2, Point(0.0, 0.0))

    def test_init(self):
        self.assertEqual(self.s.p1, Point(1.0, 2.0))
        self.assertEqual(self.s.p2, Point(3.0, 5.0))

    def test_eq(self):
        self.assertTrue(
            self.s == Segment(Point(1.0, 2.0), Point(3.0, 5.0)))
        self.assertFalse(
            self.s == Segment(Point(1.0, 3.0), Point(3.0, 5.0)))
        self.assertFalse(
            self.s == Segment(Point(1.0, 2.0), Point(3.0, 6.0)))
        self.assertFalse(
            self.s == Segment(Point(1.0, 3.0), Point(3.0, 6.0)))
        self.assertFalse(self.s == 3)

    def test_repr(self):
        self.assertEqual(self.s.__repr__(),
                         'Segment(Point(1.0, 2.0), Point(3.0, 5.0))')

    def test_vector(self):
        self.assertEqual(self.s.vector(), Vector(2.0, 3.0))

    def test_reverse(self):
        self.assertEqual(self.s.reverse(),
                         Segment(self.p2, self.p1))

    def test_length(self):
        self.assertEqual(Segment(Point(1.0, 2.0),
                                 Point(4.0, 6.0)).length(),
                         5.0)

    def test_is_orthogonal(self):
        s1 = Segment(Point(0.0, 0.0), Point(1.0, 0.0))
        s2 = Segment(Point(0.0, 0.0), Point(0.0, 1.0))
        self.assertTrue(s1.is_orthogonal(s2))
        self.assertFalse(s1.is_orthogonal(s1))

    def test_is_parallel(self):
        s1 = Segment(Point(0.0, 0.0), Point(1.0, 0.0))
        s2 = Segment(Point(0.0, 0.0), Point(0.0, 1.0))
        self.assertTrue(s1.is_parallel(s1))
        self.assertFalse(s1.is_parallel(s2))

    def test_intersect_ratio(self):
        p1 = Point(0.0, 0.0)
        p2 = Point(4.0, 0.0)
        p3 = Point(0.0, 2.0)
        p4 = Point(4.0, 2.0)
        p5 = Point(2.0, 1.0)
        p6 = Point(2.0, 0.0)

        self.assertEqual(
            Segment(p1, p4).intersect_ratio(Segment(p2, p3)),
            (0.5, 0.5))
        self.assertEqual(
            Segment(p4, p1).intersect_ratio(Segment(p2, p3)),
            (0.5, 0.5))
        self.assertEqual(
            Segment(p1, p4).intersect_ratio(Segment(p3, p2)),
            (0.5, 0.5))
        self.assertEqual(
            Segment(p4, p1).intersect_ratio(Segment(p3, p2)),
            (0.5, 0.5))
        self.assertEqual(
            Segment(p5, p4).intersect_ratio(Segment(p2, p3)),
            (0.0, 0.5))
        self.assertEqual(
            Segment(p1, p5).intersect_ratio(Segment(p2, p3)),
            (1.0, 0.5))
        self.assertEqual(
            Segment(p1, p4).intersect_ratio(Segment(p5, p3)),
            (0.5, 0.0))
        self.assertEqual(
            Segment(p1, p4).intersect_ratio(Segment(p2, p5)),
            (0.5, 1.0))
        self.assertEqual(
            Segment(p1, p6).intersect_ratio(Segment(p2, p3)),
            (2.0, 0.0))

    def test_intersects(self):
        p1 = Point(0.0, 0.0)
        p2 = Point(4.0, 0.0)
        p3 = Point(0.0, 2.0)
        p4 = Point(4.0, 2.0)
        p5 = Point(2.0, 1.0)
        p6 = Point(2.0, 0.0)
        self.assertTrue(
            Segment(p1, p4).intersects(Segment(p2, p3)))
        self.assertFalse(
            Segment(p1, p6).intersects(Segment(p2, p3)))

    def test_intersection(self):
        p1 = Point(0.0, 0.0)
        p2 = Point(4.0, 0.0)
        p3 = Point(0.0, 2.0)
        p4 = Point(4.0, 2.0)
        p5 = Point(2.0, 1.0)
        self.assertEqual(
            Segment(p1, p4).intersection(Segment(p2, p3)),
            p5)

    def test_distance_with_segment(self):
        s = Segment(Point(-1.0, 0.0), Point(1.0, 0.0))
        t = Segment(Point(0.0, -1.0), Point(0.0, 1.0))
        self.assertEqual(s.distance_with_segment(t), 0.0)
        t = Segment(Point(-1.0, 1.0), Point(1.0, 1.0))
        self.assertEqual(s.distance_with_segment(t), 1.0)
        t = Segment(Point(-2.0, 0.0), Point(0.0, 0.0))
        self.assertEqual(s.distance_with_segment(t), 0.0)
        t = Segment(Point(0.0, 1.0), Point(2.0, 3.0))
        self.assertEqual(s.distance_with_segment(t), 1.0)
        t = Segment(Point(5.0, 3.0), Point(5.0, 4.0))
        self.assertEqual(s.distance_with_segment(t), 5.0)


class TestLine(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1.0, 2.0)
        self.p2 = Point(3.0, 5.0)
        self.l = Segment(self.p1, self.p2)

    def test_init(self):
        self.assertEqual(self.l.p1, Point(1.0, 2.0))
        self.assertEqual(self.l.p2, Point(3.0, 5.0))


class TestCircle(unittest.TestCase):

    def test_init_default(self):
        c = Circle(Point(1.0, 2.0), 3.0)
        self.assertEqual(c.c, Point(1.0, 2.0))
        self.assertEqual(c.r, 3.0)

    def test_init(self):
        c = Circle(Point(1.0, 2.0), 3.0)
        self.assertEqual(c.c, Point(1.0, 2.0))
        self.assertEqual(c.r, 3.0)

    def test_eq(self):
        self.assertTrue(Circle(1.0, 2.0) == Circle(1.0, 2.0))
        self.assertFalse(Circle(1.0, 2.0) == Circle(1.0, 3.0))
        self.assertFalse(Circle(1.0, 2.0) == Circle(2.0, 2.0))
        self.assertFalse(Circle(1.0, 2.0) == Circle(2.0, 3.0))
        self.assertFalse(Circle(1.0, 2.0) == 3)

    def test_repr(self):
        c = Circle(1.0, 2.0)
        self.assertEqual(c.__repr__(), 'Circle(1.0, 2.0)')


if __name__ == "__main__":
    unittest.main()
