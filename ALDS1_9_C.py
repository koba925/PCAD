#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin
from priority_queue import NoMoreDataError
from priority_queue import PriorityQueue
from priority_queue import swap


def main():
    Q = PriorityQueue()

    for line in stdin.readlines():
        cmd = line.split()
        if cmd[0] == "insert":
            Q.insert(int(cmd[1]))
        elif cmd[0] == "extract":
            print(Q.extract_max())
        else:
            break


if __name__ == "__main__":
    main()
