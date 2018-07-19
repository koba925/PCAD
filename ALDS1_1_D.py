#! /usr/local/bin/python3
# coding: utf-8

n = int(input())

min_r = int(input())
max_margin = -1000000001

for i in range(n - 1):
    r = int(input())
    max_margin = max(r - min_r, max_margin)
    min_r = min(r, min_r)

print(max_margin)
