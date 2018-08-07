#! /usr/local/bin/python3
# coding: utf-8

from operator import add

def shape_to_slope(ch):
    if ch == "\\":
        return -1
    elif ch == "_":
        return 0
    else:
        return 1

def pool_merge(pool_area, left_x, cur_area):
    print("pool_merge: start")
    if not pool_area:
        return cur_area
    while pool_area and (pool_area[-1])[0] > len(left_x):
        print("pool_merge: merging")
        cur_area += (pool_area.pop())[1]
    return cur_area

def calc(s):
    shape = [ch for ch in s]
    slope = [shape_to_slope(ch) for ch in shape]

    left_x = []
    cur_area = 0
    pool_area = []
    for x, sl in enumerate(slope):
        if sl == -1:
            if cur_area > 0:
                pool_area.append((len(left_x), cur_area))
                cur_area = 0                
            left_x.append(x)
        elif left_x and sl == 1:
            cur_area += x - left_x.pop()
            cur_area = pool_merge(pool_area, left_x, cur_area)
            if not left_x:
                pool_area.append((len(left_x), cur_area))
                cur_area = 0
        print(x, ":", sl, left_x, cur_area, pool_area)
    if cur_area > 0:
        pool_area.append((len(left_x), cur_area))
        print("-", ":", sl, left_x, cur_area, pool_area)

    return [p[1] for p in pool_area]

def test():
    assert calc(r"\ ".strip()) == []
    assert calc(r"/ ".strip()) == []
    assert calc(r"\/ ".strip()) == [1]
    assert calc(r"\_/ ".strip()) == [2]
    assert calc(r"\// ".strip()) == [1]
    assert calc(r"\\/ ".strip()) == [1]
    assert calc(r"\\// ".strip()) == [4]
    assert calc(r"\\//\\// ".strip()) == [4, 4]
    assert calc(r"\\/\// ".strip()) == [7]
    assert calc(r"\\/_\// ".strip()) == [8]
    assert calc(r"\//\\/ ".strip()) == [1, 1]
    assert calc(r"\//_\\/ ".strip()) == [1, 1]
    assert calc(r"\//\\// ".strip()) == [1, 4]
    assert calc(r"\///\\\// ".strip()) == [1, 4]
    assert calc(r"\///\\\//\ ".strip()) == [1, 4]
    exit()

# test()

pool_area = calc(input())
print(sum(pool_area))
print(len(pool_area), *pool_area)