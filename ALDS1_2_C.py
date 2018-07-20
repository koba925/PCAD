#! /usr/local/bin/python3
# coding: utf-8

def swap(c, i, j):
    t = c[i]
    c[i] = c[j]
    c[j] = t

def bubble_sort(c):
    for i in range(len(c) - 1):
        for j in range(i + 1, len(c)):
            print(i, j)
            if c[i] > c[j]:
                swap(c, i, j)
    return c

print(bubble_sort([4,2,5,6,1,3]))
