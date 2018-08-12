#! /usr/local/bin/python3
# coding: utf-8

def can_make_sum(A, k, m):
    #print(A, k, m)
    if m == 0:
        return True
    elif m < 0 or k == len(A):
        return False
    else: 
        return (can_make_sum(A, k + 1, m - A[k]) or
                can_make_sum(A, k + 1, m))

def solve():
    _ = int(input())
    A = [int(x) for x in input().split()]
    _ = int(input())
    M = [int(x) for x in input().split()]

    for m in M:
        print("yes" if can_make_sum(A, 0, m) else "no")

def test():
    assert can_make_sum([1, 3, 7], 0, 1)
    assert can_make_sum([1, 3, 7], 0, 3)
    assert can_make_sum([1, 3, 7], 0, 7)
    assert can_make_sum([1, 3, 7], 0, 4)
    assert can_make_sum([1, 3, 7], 0, 8)
    assert can_make_sum([1, 3, 7], 0, 10)
    assert can_make_sum([1, 3, 7], 0, 11)
    assert not can_make_sum([1, 3, 7], 0, 2)
    assert not can_make_sum([1, 3, 7], 0, 5)
    assert not can_make_sum([1, 3, 7], 0, 12)

# test()
# exit()

solve()
