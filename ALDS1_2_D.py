#! /usr/local/bin/python3
# coding: utf-8

def insertion_sort(A, g):
    global cnt
    for i in range(g, len(A)):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cnt += 1
        A[j + g] = v

def shell_sort(A):
    global cnt, G
    for g in G:
        insertion_sort(A, g)

n = int(input())

G = [1]
for i in range(1, 100):
    g = 3 * G[i - 1] + 1
    if g > n:
        break
    G.append(g)
G.reverse()

cnt = 0
A = []
for i in range(n):
    A = A + [int(input())]

shell_sort(A)

print(len(G))
print(" ".join([str(i) for i in G]))
print(cnt)
[print(i) for i in A]
