#! /usr/local/bin/python3
# coding: utf-8

from bisect import bisect_left


def count_inversion(A):
    cnt = 0
    for i in reversed(range(len(A) - 1)):
        j = bisect_left(A, A[i], i + 1, len(A))
        cnt += j - i - 1
        tmp = A[i]
        del A[i]
        A.insert(j - 1, tmp)
    return cnt


def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    print(count_inversion(A))


main()
