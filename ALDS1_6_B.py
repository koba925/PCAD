#! /usr/local/bin/python3
# coding: utf-8

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1

def bracketify(A, i, q):
    return "[" + str(A[i]) + "]" if i == q else str(A[i])

def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    q = partition(A, 0, n - 1)
    print(*[bracketify(A, i, q) for i in range(n)])

main()
