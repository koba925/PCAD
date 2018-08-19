#! /usr/local/bin/python3
# coding: utf-8

from math import inf

c = 0

def merge(A, left, mid, right):
    global c
    
    # print(A, left, mid, right)
    L = A[left:mid]; L.append(inf)
    R = A[mid:right]; R.append(inf)
    # print(L)
    # print(R)
    i = iter(L); l = next(i)
    j = iter(R); r = next(j)
    for k in range(left, right):
        # print(l, r)
        c += 1
        if l <= r:
            A[k] = l
            l = next(i)
        else:
            A[k] = r
            r = next(j)

def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)

def main():
    n = int(input())
    S = [int(x) for x in input().split()]
    merge_sort(S, 0, n)
    print(*S)
    print(c)

main()
