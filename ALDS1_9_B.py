#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


def heap_size(A):
    return len(A) - 1


def parent_node(k):
    return k // 2


def left_node(k):
    return 2 * k


def right_node(k):
    return 2 * k + 1


def max_heapify(A, i):
    l = left_node(i)
    r = right_node(i)

    if l <= heap_size(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size(A) and A[r] > A[largest]:
        largest = r

    if largest != i:
        swap(A, i, largest)
        max_heapify(A, largest)


def build_max_heap(A):
    for i in reversed(range(1, heap_size(A) // 2 + 1)):
        max_heapify(A, i)


def print_heap(A):
    for i in range(1, heap_size(A) + 1):
        print(" {}".format(A[i]), end="")
    print()


def main():
    _ = int(input())
    A = [None] + [int(x) for x in input().split()]

    build_max_heap(A)
    print_heap(A)


main()
