#! /usr/local/bin/python3
# coding: utf-8

from sys import stdin
from collections import deque

def main():
    n = int(input())
    dll = deque()

    for _ in range(n):
        line = stdin.readline().split()
        if line[0] == "insert":
            dll.appendleft(int(line[1]))
        elif line[0] == "delete":
            try:
                dll.remove(int(line[1]))
            except ValueError:
                None
        elif line[0] == "deleteFirst":
            dll.popleft()
        elif line[0] == "deleteLast":
            dll.pop()

    print((" ".join(map(str, dll))))

main()
