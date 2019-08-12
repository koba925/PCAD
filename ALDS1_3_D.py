#! /usr/local/bin/python3
# coding: utf-8

def calc(shape):
    left_x = []
    pool_area = []
    for x, sh in enumerate(shape):
        if sh == "\\":
            left_x.append(x)
        elif left_x and sh == "/":
            lx = left_x.pop()
            area = x - lx
            while pool_area and (pool_area[-1])[0] > lx:
                area += (pool_area.pop())[1]
            pool_area.append((lx, area))
        # print(x, ":", sh, left_x, pool_area)

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
# exit()

pool_area = calc(input())
print(sum(pool_area))
print(len(pool_area), *pool_area)