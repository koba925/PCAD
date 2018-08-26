#! /usr/local/bin/python3
# coding: utf-8

from math import inf

inv = 0


def merge(A, left, mid, right):
    global inv

    L = A[left:mid]
    L.append(inf)
    R = A[mid:right]
    R.append(inf)
    i = j = 0
    for k in range(left, right):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            inv += len(L) - i - 1
            A[k] = R[j]
            j += 1


def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    merge_sort(A, 0, n)
    print(inv)


main()
