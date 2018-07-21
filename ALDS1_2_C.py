#! /usr/local/bin/python3
# coding: utf-8

def swap(c, i, j):
    t = c[i]
    c[i] = c[j]
    c[j] = t

def bubble_sort(c, f):
    for i in range(len(c) - 1):
        for j in range(i + 1, len(c)):
            # print(i, j)
            if f(c[i]) > f(c[j]):
                swap(c, i, j)
    return c

def insertion_sort(c, f):
    for i in range(1, len(c)):
        w = c[i]
        j = i - 1
        while j >= 0 and f(c[j]) > f(w):
            c[j + 1] = c[j]
            j -= 1
        c[j + 1] = w
    return c

def selection_sort(c, f):
    for i in range(len(c) - 1):
        minj = i
        for j in range(i + 1, len(c)):
            if f(c[j]) < f(c[minj]):
                minj = j
        swap(c, i, minj)
    return c

#def is_stable(c, s): 

print(bubble_sort(['C4', 'H3', 'S3', 'C1', 'D2'], lambda x: x[1]))
print(bubble_sort(['H3', 'S3', 'D2', 'C4', 'C1'], lambda x: x[1]))
print(bubble_sort(['C1', 'C4', 'D2', 'H3', 'S3'], lambda x: x[1]))

print(insertion_sort(['C4', 'H3', 'S3', 'C1', 'D2'], lambda x: x[1]))
print(insertion_sort(['H3', 'S3', 'D2', 'C4', 'C1'], lambda x: x[1]))
print(insertion_sort(['C1', 'C4', 'D2', 'H3', 'S3'], lambda x: x[1]))

print(selection_sort(['C4', 'H3', 'S3', 'C1', 'D2'], lambda x: x[1]))
print(selection_sort(['H3', 'S3', 'D2', 'C4', 'C1'], lambda x: x[1]))
print(selection_sort(['C1', 'C4', 'D2', 'H3', 'S3'], lambda x: x[1]))


