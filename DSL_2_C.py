import copy
from sys import stdin, setrecursionlimit


class Node():
    def __init__(self):
        self.location = None
        self.p = self.l = self.r = None

    def __repr__(self):
        return "Node({}, {}, {}, {}, {})".format(
            self.location, self.p, self.l, self.r)


class Point():
    MAX = 1000000

    def __init__(self, id=None, x=None, y=None):
        self.id = id
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.id < other.id

    def __repr__(self):
        return "Point({}, {}, {})".format(
            self.id, self.x, self.y)


np = 0
P = []
T = []


def read_points():
    global P, T

    n = int(stdin.readline())
    for i in range(n):
        x, y = [int(x) for x in stdin.readline().split()]
        P.append(Point(i, x, y))
        T.append(Node())
    return n


def make_kd_tree(l, r, depth):
    global np, P, T

    if l >= r:
        return None

    mid = (l + r) // 2
    t = np
    np += 1

    if depth % 2 == 0:
        P[l:r] = sorted(P[l:r], key=lambda p: p.x)
    else:
        P[l:r] = sorted(P[l:r], key=lambda p: p.y)
    T[t].location = mid
    T[t].l = make_kd_tree(l, mid, depth + 1)
    T[t].r = make_kd_tree(mid + 1, r, depth + 1)

    return t


def find(v, sx, tx, sy, ty, depth, ans):
    global P, T

    x = P[T[v].location].x
    y = P[T[v].location].y

    if sx <= x <= tx and sy <= y <= ty:
        ans.append(P[T[v].location])

    if depth % 2 == 0:
        if T[v].l is not None:
            if sx <= x:
                find(T[v].l, sx, tx, sy, ty, depth + 1, ans)
        if T[v].r is not None:
            if x <= tx:
                find(T[v].r, sx, tx, sy, ty, depth + 1, ans)
    else:
        if T[v].l is not None:
            if sy <= y:
                find(T[v].l, sx, tx, sy, ty, depth + 1, ans)
        if T[v].r is not None:
            if y <= ty:
                find(T[v].r, sx, tx, sy, ty, depth + 1, ans)


def process_queries(root):
    global P

    q = int(stdin.readline())
    for i in range(q):
        sx, tx, sy, ty = [int(x) for x in stdin.readline().split()]
        ans = []
        find(root, sx, tx, sy, ty, 0, ans)
        [print(a.id) for a in sorted(ans)]
        print()


def main():
    setrecursionlimit(100)
    n = read_points()
    root = make_kd_tree(0, n, 0)
    process_queries(root)


if __name__ == '__main__':
    main()
