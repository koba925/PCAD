#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from random import randrange
from priority_queue import NoMoreDataError
from priority_queue import PriorityQueue
from priority_queue import swap


class TestPriorityQueue(unittest.TestCase):

    def test_sequence1(self):
        Q = PriorityQueue()
        with self.assertRaises(NoMoreDataError):
            Q.extract_max()

    def test_sequence2(self):
        Q = PriorityQueue()
        Q.insert(1)
        Q.insert(2)
        Q.insert(3)
        self.assertEqual(Q.extract_max(), 3)
        self.assertEqual(Q.extract_max(), 2)
        self.assertEqual(Q.extract_max(), 1)
        with self.assertRaises(NoMoreDataError):
            Q.extract_max()

    def test_sequence3(self):
        Q = PriorityQueue([1])
        self.assertEqual(Q.extract_max(), 1)
        with self.assertRaises(NoMoreDataError):
            Q.extract_max()

    def test_sequence4(self):
        Q = PriorityQueue([1, 2, 3])
        self.assertEqual(Q.extract_max(), 3)
        self.assertEqual(Q.extract_max(), 2)
        self.assertEqual(Q.extract_max(), 1)
        with self.assertRaises(NoMoreDataError):
            Q.extract_max()

    def _random_array(self, max, n):
        A = [randrange(max) for _ in range(n)]
        for i in range(n):
            swap(A, i, randrange(n))
        return A

    def _test_build_max_heap(self, A):
        Q = PriorityQueue(A)
        R = Q.to_array()
        self.assertEqual(list(reversed(sorted(A))), R)

    def _test_insert(self, A):
        Q = PriorityQueue()
        for n in A:
            Q.insert(n)
        R = Q.to_array()
        self.assertEqual(list(reversed(sorted(A))), R)

    def test_random_build_max_heap(self):
        for i in range(1000):
            self._test_build_max_heap(self._random_array(15, 10))

    def test_random_insert(self):
        for i in range(1000):
            self._test_insert(self._random_array(15, 10))


if __name__ == "__main__":
    unittest.main()
