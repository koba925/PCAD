#! /usr/local/bin/python3
# coding: utf-8

from bisect import bisect_left

def search(S, y):
    pos = bisect_left(S, y)
    return S[pos] == y

def count(S, T):
    c = 0
    for y in T:
        if search(S, y):
            c += 1
    return c

_ = int(input())
S = [int(x) for x in input().split()]

_ = int(input())
T = [int(y) for y in input().split()]

print(count(S, T))
