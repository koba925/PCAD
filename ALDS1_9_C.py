#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin


def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


def null_heap():
    return [None]


def parent_node(k):
    return k // 2


def left_node(k):
    return 2 * k


def right_node(k):
    return 2 * k + 1


def sibling_node(k):
    assert k > 1

    parent = parent_node(k)
    if is_left(k):
        return right_node(parent)
    else:
        return left_node(parent)


def last_node(S):
    return len(S) - 1


def is_empty(S):
    return len(S) == 1


def is_left(i):
    return i % 2 == 0


def insert(S, k):

    def rec(i):
        nonlocal S

        if i == 1:
            return

        p = parent_node(i)
        if S[p] < S[i]:
            swap(S, p, i)
            rec(p)

    S.append(k)
    rec(last_node(S))


def max_heapify(S, i):
    l = left_node(i)
    r = right_node(i)
    if l <= last_node(S) and S[l] > S[i]:
        largest = l
    else:
        largest = i
    if r <= last_node(S) and S[r] > S[largest]:
        largest = r

    if largest != i:
        swap(S, i, largest)
        max_heapify(S, largest)


def extract_max(S):
    if last_node(S) == 1:
        return S.pop()
    else:
        k = S[1]
        S[1] = S.pop()
        max_heapify(S, 1)
        return k


def extract_max_old(S):

    def rec(i, k):
        nonlocal S

        if i == 1:
            tmp = S[i]
            S[i] = k
            return tmp

        parent = parent_node(i)
        sibling = sibling_node(i)
        larger = i if S[i] > S[sibling] else sibling
        tmp = S[larger]
        S[larger] = k
        return rec(parent, tmp)

    last = last_node(S)
    if last == 1:
        return S.pop()

    parent = parent_node(last)
    if is_left(last):
        return rec(parent, S.pop())
    else:
        left = left_node(parent)
        if S[left] > S[last]:
            v = S[left]
            S[left] = S.pop()
            return rec(parent, v)
        else:
            return rec(parent, S.pop())


def print_heap(A):
    for i in range(1, last_node(A) + 1):
        print(" {}".format(A[i]), end="")
    print()


from random import randrange


def random_array(n):
    A = list(range(n))
    for i in range(n):
        swap(A, i, randrange(n))
    return A


def from_array(S, A):
    for k in A:
        insert(S, k)


def from_heap(S):
    R = []
    while not is_empty(S):
        R.append(extract_max(S))
    return R


def test_a_case():
    A = random_array(15)
    S = null_heap()
    from_array(S, A)
    R = from_heap(S)
    assert list(reversed(sorted(A))) == R, \
        "\nA={}\nR={}".format(A, R)


def test():
    for i in range(10000):
        test_a_case()


def main():
    S = null_heap()

    for line in stdin:
        cmd = line.split()
        if cmd[0] == "insert":
            insert(S, int(cmd[1]))
        elif cmd[0] == "extract":
            print(extract_max(S))
        else:
            break


main()
