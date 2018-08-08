#! /usr/local/bin/python3
# coding: utf-8

def count(s, t):
    c = 0
    for x in t:
        for y in s:
            if x == y:
                c += 1
                break
    return c

_ = int(input())
s = [int(x) for x in input().split()]

_ = int(input())
t = [int(x) for x in input().split()]

print(count(s, t))
