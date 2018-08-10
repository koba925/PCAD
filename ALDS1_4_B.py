#! /usr/local/bin/python3
# coding: utf-8

def search(S, y):
    left = 0; right = len(S) - 1
    while left <= right:
        mid = (left + right) // 2
        if S[mid] == y: 
            return True
        if S[mid] < y:
            left = mid + 1
        else:
            right = mid - 1
    return False

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
