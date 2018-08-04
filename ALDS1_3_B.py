#! /usr/local/bin/python3
# coding: utf-8

from collections import deque

def main():
    n, q = [int(x) for x in input().split()]

    proc = deque()

    for i in range(n):
        name, ptime = input().split()
        proc.appendleft((name, int(ptime)))

    time = 0
    while proc:
        name, ptime = proc.pop()
        time += min(q, ptime)
        ptime -= min(q, ptime)
        if ptime <= 0:
            print(name, time)
        else:
            proc.appendleft((name, ptime))

main()