#! /usr/local/bin/python3
# coding: utf-8

from sys import stdin

cnt = 0


def swap(A, i, j):
    global cnt

    cnt += j - i
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    print(*A, i, j)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1


def count_inversion(A, p, r):
    if p < r:
        q = partition(A, p, r)
        count_inversion(A, p, q - 1)
        count_inversion(A, q + 1, r)


def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    count_inversion(A, 0, n - 1)
    print(cnt)


main()
