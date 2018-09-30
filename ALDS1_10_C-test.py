#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from sys import setrecursionlimit
from ALDS1_10_C import lcs

setrecursionlimit(10000)


class TestLcs(unittest.TestCase):
    def test_lcs(self):
        self.assertEqual(lcs("", ""), 0)
        self.assertEqual(lcs("T", ""), 0)
        self.assertEqual(lcs("", "T"), 0)
        self.assertEqual(lcs("T", "T"), 1)
        self.assertEqual(lcs("TA", "T"), 1)
        self.assertEqual(lcs("AT", "T"), 1)
        self.assertEqual(lcs("T", "TA"), 1)
        self.assertEqual(lcs("T", "AT"), 1)
        self.assertEqual(lcs("TA", "AT"), 1)
        self.assertEqual(lcs("AT", "TA"), 1)
        self.assertEqual(lcs("TA", "TA"), 2)
        self.assertEqual(lcs("TCCAGATGG", "TCACA"), 4)


if __name__ == '__main__':
    unittest.main()
