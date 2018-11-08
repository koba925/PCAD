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

    def rec(l, r, depth):
        if l >= r:
            return None

        mid = (l + r) // 2

        if depth % 2 == 0:
            P[l:r] = sorted(P[l:r], key=lambda p: p.x)
        else:
            P[l:r] = sorted(P[l:r], key=lambda p: p.y)

        node = Node()
        node.location = mid
        node.l = rec(l, mid, depth + 1)
        node.r = rec(mid + 1, r, depth + 1)

        return node

    root = rec(0, len(P), 0)
    return root


def find(P, root, sx, tx, sy, ty):
    ans = []

    def rec(node, depth):
        nonlocal P, sx, tx, sy, ty, ans

        x = P[node.location].x
        y = P[node.location].y

        if sx <= x <= tx and sy <= y <= ty:
            ans.append(P[node.location])

        if depth % 2 == 0:
            if node.l is not None and sx <= x:
                rec(node.l, depth + 1)
            if node.r is not None and x <= tx:
                rec(node.r, depth + 1)
        else:
            if node.l is not None and sy <= y:
                rec(node.l, depth + 1)
            if node.r is not None and y <= ty:
                rec(node.r, depth + 1)

    rec(root, 0)
    return ans


def process_queries(P, root):
    q = int(stdin.readline())
    for i in range(q):
        sx, tx, sy, ty = [int(x) for x in stdin.readline().split()]
        ans = find(P, root, sx, tx, sy, ty)
        [print(a.id) for a in sorted(ans)]
        print()


def main():
    P = read_points()
    root = make_kd_tree(P)
    process_queries(P, root)


if __name__ == '__main__':
    main()
