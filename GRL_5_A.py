from collections import deque


class Node():
    def __init__(self, key):
        self.key = key
        self.passed = False
        self.adj = []

    def __repr__(self):
        return "Node({}, {}, {})".format(
            self.key,
            [(a.key, w) for a, w in self.adj])


def read_inputs():
    n = int(input())
    T = [Node(i) for i in range(n)]
    for _ in range(n - 1):
        s, t, w = [int(x) for x in input().split()]
        T[s].adj.append((T[t], w))
        T[t].adj.append((T[s], w))
    return T


def furthest(T, s):
    for v in T:
        v.passed = False

    fur = -1
    fur_v = None
    Q = deque()
    Q.append((s, 0))

    while len(Q) > 0:
        v, vr = Q.popleft()
        if vr > fur:
            fur = vr
            fur_v = v
        v.passed = True
        for a, w in v.adj:
            if not a.passed:
                Q.append((a, vr + w))

    return fur, fur_v


def tree_diameter(T):
    _, s = furthest(T, T[0])
    fur, _ = furthest(T, s)
    return fur


def main():
    T = read_inputs()
    r = tree_diameter(T)
    print(r)


if __name__ == "__main__":
    main()
