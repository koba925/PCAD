#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


class NoMoreDataError(Exception):
    pass


class PriorityQueue():
    def __init__(self, elems=[]):
        self.A = [None] + elems
        self._build_max_heap()

    def __repr__(self):
        return str(self.A[1:])

    def is_empty(self):
        return len(self.A) == 1

    def insert(self, k):
        self.A.append(k)

        i = self._last()
        if i == 1:
            return

        while i > 1:
            p = self._parent(i)
            if self.A[p] >= self.A[i]:
                break
            swap(self.A, p, i)
            i = p

    def extract_max(self):
        if self._last() == 0:
            raise NoMoreDataError
        if self._last() == 1:
            return self.A.pop()
        else:
            k = self.A[1]
            self.A[1] = self.A.pop()
            self._max_heapify(1)
            return k

    def to_array(self):
        R = []
        while not self.is_empty():
            R.append(self.extract_max())
        return R

    def _parent(self, k):
        return k // 2

    def _left(self, k):
        return 2 * k

    def _right(self, k):
        return 2 * k + 1

    def _last(self):
        return len(self.A) - 1

    def _max_heapify(self, i):
        l = self._left(i)
        r = self._right(i)
        if l <= self._last() and \
           self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i
        if r <= self._last() and self.A[r] > self.A[largest]:
            largest = r

        if largest != i:
            swap(self.A, i, largest)
            self._max_heapify(largest)

    def _build_max_heap(self):
        for i in reversed(range(1, self._last() // 2 + 1)):
            self._max_heapify(i)
