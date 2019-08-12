#! /usr/local/bin/python3
# coding: utf-8

def swap(c, i, j):
    t = c[i]
    c[i] = c[j]
    c[j] = t

def bubble_sort(cs, f):
    c = cs[:]
    for i in range(len(c) - 1):
        for j in range(len(c) - 1, i, -1):
            if f(c[j - 1]) > f(c[j]):
                swap(c, j - 1, j)
            # print(i, j, c)
    return c

def insertion_sort(cs, f):
    c = cs[:]
    for i in range(1, len(c)):
        w = c[i]
        j = i - 1
        while j >= 0 and f(c[j]) > f(w):
            c[j + 1] = c[j]
            j -= 1
        c[j + 1] = w
    return c

def selection_sort(cs, f):
    c = cs[:]
    for i in range(len(c)):
        minj = i
        for j in range(i, len(c)):
            if f(c[j]) < f(c[minj]):
                minj = j
        swap(c, i, minj)
        # print(c)
    return c

def to_group(c):
    b = {}
    for i in c:
        if not(i[1] in b):
            b[i[1]] = [i]
        else:
            b[i[1]] = b[i[1]] + [i]
    return b

def is_stable(c, s): 
    bc = to_group(c)
    bs = to_group(s(c, lambda x: x[1]))
    # print(bc)
    # print(bs)
    for k in bc:
        if bc[k] != bs[k]:
            return "Not stable"
    return "Stable"

n = int(input())
c = input().split()

print(" ".join(bubble_sort(c, lambda x: x[1])))
print(is_stable(c, bubble_sort))

print(" ".join(selection_sort(c, lambda x: x[1])))
print(is_stable(c, selection_sort))

exit()

print(is_stable(['C4', 'H3', 'S3', 'C1', 'D2'], bubble_sort))
print(is_stable(['C4', 'H3', 'S3', 'C1', 'D2'], insertion_sort))
print(is_stable(['C4', 'H3', 'S3', 'C1', 'D2'], selection_sort))

print(bubble_sort(['C4', 'H3', 'S3', 'C1', 'D2'], lambda x: x[1]))

print(bubble_sort(['C4', 'H3', 'S3', 'C1', 'D2'], lambda x: x[1]))
print(bubble_sort(['H3', 'S3', 'D2', 'C4', 'C1'], lambda x: x[1]))
print(bubble_sort(['C1', 'C4', 'D2', 'H3', 'S3'], lambda x: x[1]))

print(insertion_sort(['C4', 'H3', 'S3', 'C1', 'D2'], lambda x: x[1]))
print(insertion_sort(['H3', 'S3', 'D2', 'C4', 'C1'], lambda x: x[1]))
print(insertion_sort(['C1', 'C4', 'D2', 'H3', 'S3'], lambda x: x[1]))

print(selection_sort(['C4', 'H3', 'S3', 'C1', 'D2'], lambda x: x[1]))
print(selection_sort(['H3', 'S3', 'D2', 'C4', 'C1'], lambda x: x[1]))
print(selection_sort(['C1', 'C4', 'D2', 'H3', 'S3'], lambda x: x[1]))
