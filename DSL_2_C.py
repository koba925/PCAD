import copy
from sys import stdin, setrecursionlimit


class Area():
    MAX = 2000000000
    MIN = -MAX

    def __init__(self):
        self.sx = self.sy = Area.MIN
        self.tx = self.ty = Area.MAX
        self.indices = None
        self.lb_area = self.rt_area = None

    def __repr__(self):
        return "Area({}, {}, {}, {}, {}, {}, {})".format(
            self.sx, self.sy, self.tx, self.ty,
            self.indices, self.lb_area, self.rt_area)


def tr(x):
    return x * 2


def read_points():
    n = int(stdin.readline())
    points = []
    for _ in range(n):
        x, y = [int(x) for x in stdin.readline().split()]
        points.append((x * 2, y * 2))
    return points


# dir = 0 -> 左右に分割
# dir = 1 -> 上下に分割

from random import randrange


def find_mid(points, indices, dir):
    # s = sorted(set(points[x][dir] for x in indices))
    # return s[len(s)//2]
    return points[indices[randrange(len(indices))]][dir]


def partition(points, mid, indices, dir):
    lb_indices = []
    rt_indices = []
    for i in indices:
        if points[i][dir] < mid:
            lb_indices.append(i)
        else:
            rt_indices.append(i)
    return lb_indices, rt_indices


def divide_area(points, area, dir):

    if len(area.indices) <= 1:
        return

    # area.indices.sort(key=lambda x: points[x][dir])
    mid = find_mid(points, area.indices, dir)
    lb_indices, rt_indices = partition(points, mid, area.indices, dir)

    lb_area = rt_area = None
    if lb_indices:
        lb_area = copy.copy(area)
        if dir == 0:
            lb_area.tx = mid
        else:
            lb_area.ty = mid
        lb_area.indices = lb_indices
        divide_area(points, lb_area, 1-dir)
    if rt_indices:
        rt_area = copy.copy(area)
        if dir == 0:
            rt_area.sx = mid
        else:
            rt_area.sy = mid
        rt_area.indices = rt_indices
        divide_area(points, rt_area, 1-dir)
    area.lb_area = lb_area
    area.rt_area = rt_area


def make_area_tree(points):
    tree = Area()
    tree.indices = list(range(len(points)))
    divide_area(points, tree, 0)
    return tree


def pick_points(sx, tx, sy, ty, points):
    for i in range(len(points)):
        if sx <= points[i][0] <= tx and \
           sy <= points[i][1] <= ty:
            print(i)
    print()


def find_points(sx, tx, sy, ty, points, tree):

    found = []

    def rec(area):
        nonlocal points, found

        if tx < area.sx or area.tx < sx or \
           ty < area.sy or area.ty < sy:
            return
        if sx < area.sx and area.tx < tx and \
           sy < area.sy and area.ty < ty:
            found += area.indices
            return
        if area.lb_area is None and area.rt_area is None:
            if area.indices:
                i = area.indices[0]
                p = points[i]
                if sx < p[0] < tx and sy < p[1] < ty:
                    found.append(i)
            return
        if area.lb_area is not None:
            rec(area.lb_area)
        if area.rt_area is not None:
            rec(area.rt_area)

    rec(tree)
    found.sort()
    return found


def process_queries(points, tree):
    q = int(stdin.readline())
    for i in range(q):
        sx, tx, sy, ty = [int(x) for x in stdin.readline().split()]
        found = find_points(sx * 2 - 1, tx * 2 + 1,
                            sy * 2 - 1, ty * 2 + 1, points, tree)
        print(*found, sep="\n")
        if found:
            print()


def main():
    setrecursionlimit(100)
    points = read_points()
    tree = make_area_tree(points)
    process_queries(points, tree)


"""
points = [(2, 1), (2, 2), (4, 2), (6, 2), (3, 3), (5, 4)]
tree = make_area_tree(points)
print(find_points(1, 6, 0, 3, points, tree))
exit()
"""

if __name__ == '__main__':
    main()
