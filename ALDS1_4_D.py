#! /usr/local/bin/python3
# coding: utf-8

from math import floor
from sys import stdin

def allocate(n, k, w, P):
    n_truck = 1
    load = 0
    for wt in w:
        # print(n_truck, load, wt, P)
        if load + wt > P:
            n_truck += 1
            if n_truck > k:
                return False
            load = 0
        load += wt
    return True

def main():
    n, k = [int(x) for x in stdin.readline().split()]
    w = [int(x) for x in stdin]
    min_P = max(max(w), floor(sum(w) / k))
    max_P = sum(w)
 
    while min_P < max_P:
        mid_P = (min_P + max_P) // 2
        if allocate(n, k, w, mid_P):
            max_P = mid_P
        else:
            min_P = mid_P + 1
    
    print(min_P)

main()
