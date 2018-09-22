#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin


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


from random import randrange


def test_a_case_1(A):
    Q = PriorityQueue(A)
    R = Q.to_array()
    assert list(reversed(sorted(A))) == R, \
        "\nA={}\nR={}".format(A, R)


def test_a_case_2(A):
    Q = PriorityQueue([])
    for n in A:
        Q.insert(n)
    R = Q.to_array()
    assert list(reversed(sorted(A))) == R, \
        "\nA={}\nR={}".format(A, R)


def random_array(max, n):
    A = [randrange(max) for _ in range(n)]
    for i in range(n):
        swap(A, i, randrange(n))
    return A


def test_a_random_case_1():
    test_a_case_1(random_array(15, 10))


def test_a_random_case_2():
    test_a_case_2(random_array(15, 10))


def test():
    for i in range(10000):
        test_a_random_case_1()
        test_a_random_case_2()


def main():
    Q = PriorityQueue()
    lines = stdin.readlines()

    for line in lines:
        cmd = line.split()
        if cmd[0] == "insert":
            Q.insert(int(cmd[1]))
        elif cmd[0] == "extract":
            print(Q.extract_max())
        else:
            break


main()
