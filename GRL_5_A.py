from sys import setrecursionlimit


class Node():
    def __init__(self, key):
        self.key = key
        self.indeg = 0
        self.passed = False
        self.adj = []

    def __repr__(self):
        return "Node({}, {}, {})".format(
            self.key, self.indeg,
            [(a.key, w) for a, w in self.adj])


def read_inputs():
    n = int(input())
    T = [Node(i) for i in range(n)]
    for _ in range(n - 1):
        s, t, w = [int(x) for x in input().split()]
        T[s].indeg += 1
        T[t].indeg += 1
        T[s].adj.append((T[t], w))
        T[t].adj.append((T[s], w))
    return T


cache = {}


def furthest(T, s):

    def rec(v):
        v.passed = True
        fur = 0
        for a, w in v.adj:
            if not a.passed:
                if (v, a) in cache:
                    d = cache[(v, a)]
                else:
                    d = rec(a) + w
                    cache[(v, a)] = d
                fur = max(fur, d)
        return fur

    for v in T:
        v.passed = False
    return rec(s)


def tree_diameter(T):
    return max([0] + [furthest(T, s) for s in T if s.indeg == 1])


def main():
    setrecursionlimit(100000)
    T = read_inputs()
    r = tree_diameter(T)
    print(r)


if __name__ == "__main__":
    main()
