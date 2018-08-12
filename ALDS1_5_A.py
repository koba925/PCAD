#! /usr/local/bin/python3
# coding: utf-8

def can_make_sum(A, m):
    if m == 0:
        return True
    elif m < 0 or not A:
        return False
    else: 
        return (can_make_sum(A[1:], m - A[0]) or
                can_make_sum(A[1:], m))

def solve():
    n = int(input())
    A = [int(x) for x in input().split()]
    q = int(input())
    M = [int(x) for x in input().split()]

    for m in M:
        print("yes" if can_make_sum(A, m) else "no")

def test():
    assert can_make_sum([1, 3, 7], 1)
    assert can_make_sum([1, 3, 7], 3)
    assert can_make_sum([1, 3, 7], 7)
    assert can_make_sum([1, 3, 7], 4)
    assert can_make_sum([1, 3, 7], 8)
    assert can_make_sum([1, 3, 7], 10)
    assert can_make_sum([1, 3, 7], 11)
    assert not can_make_sum([1, 3, 7], 2)
    assert not can_make_sum([1, 3, 7], 5)
    assert not can_make_sum([1, 3, 7], 12)

# test()
# exit()

solve()
