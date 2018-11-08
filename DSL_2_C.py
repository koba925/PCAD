from sys import stdin


class Node():
    def __init__(self):
        self.location = None
        self.l = self.r = None

    def __repr__(self):
        return "Node({}, {}, {}, {}, {})".format(
            self.location, self.p, self.l, self.r)


class Point():
    def __init__(self, id=None, x=None, y=None):
        self.id = id
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.id < other.id

    def __repr__(self):
        return "Point({}, {}, {})".format(
            self.id, self.x, self.y)


def read_points():
    n = int(stdin.readline())
    P = []
    for i in range(n):
        x, y = [int(x) for x in stdin.readline().split()]
        P.append(Point(i, x, y))
    return P


def make_kd_tree(P):
    T = [Node() for _ in range(len(P))]
    np = 0

    def rec(l, r, depth):
        nonlocal np

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
        T[t].l = rec(l, mid, depth + 1)
        T[t].r = rec(mid + 1, r, depth + 1)

        return t

    root = rec(0, len(P), 0)
    return root, T


def find(P, T, root, sx, tx, sy, ty):
    ans = []

    def rec(v, depth):
        nonlocal P, T, sx, tx, sy, ty, ans

        x = P[T[v].location].x
        y = P[T[v].location].y

        if sx <= x <= tx and sy <= y <= ty:
            ans.append(P[T[v].location])

        if depth % 2 == 0:
            if T[v].l is not None:
                if sx <= x:
                    rec(T[v].l, depth + 1)
            if T[v].r is not None:
                if x <= tx:
                    rec(T[v].r, depth + 1)
        else:
            if T[v].l is not None:
                if sy <= y:
                    rec(T[v].l, depth + 1)
            if T[v].r is not None:
                if y <= ty:
                    rec(T[v].r, depth + 1)

    rec(root, 0)
    return ans


def process_queries(P, T, root):
    q = int(stdin.readline())
    for i in range(q):
        sx, tx, sy, ty = [int(x) for x in stdin.readline().split()]
        ans = find(P, T, root, sx, tx, sy, ty)
        [print(a.id) for a in sorted(ans)]
        print()


def main():
    P = read_points()
    root, T = make_kd_tree(P)
    process_queries(P, T, root)


if __name__ == '__main__':
    main()
