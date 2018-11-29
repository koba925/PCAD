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


def furthest(T, s):

    for v in T:
        v.passed = False
    fur = -1
    fur_v = None
    S = []
    S.append((s, 0))

    while S != []:
        v, vr = S.pop()
        v.passed = True
        is_end = True
        for a, w in v.adj:
            if not a.passed:
                S.append((a, vr + w))
                is_end = False
        if is_end and vr > fur:
            fur = vr
            fur_v = v

    return fur, fur_v


def tree_diameter(T):

    if len(T) == 1:
        return 0

    s = [s for s in T if s.indeg == 1][0]
    fur, s2 = furthest(T, s)
    fur, fur_v = furthest(T, s2)

    return fur


def main():
    T = read_inputs()
    r = tree_diameter(T)
    print(r)


if __name__ == "__main__":
    main()
