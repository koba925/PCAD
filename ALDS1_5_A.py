#! /usr/local/bin/python3
# coding: utf-8

def solve():
    def can_make_sum(k, m):
        def cmi(k, m):
            if m == 0:
                return True
            elif m < 0 or k == n:
                return False
            else: 
                return (can_make_sum(k + 1, m - A[k]) or
                        can_make_sum(k + 1, m))

        if (k, m) not in cache:
            cache[(k, m)] = cmi(k, m)
        return cache[(k, m)]

    cache = {}
    n = int(input())
    A = [int(x) for x in input().split()]
    _ = int(input())
    M = [int(x) for x in input().split()]

    for m in M:
        print("yes" if can_make_sum(0, m) else "no")

solve()
