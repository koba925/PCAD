class DisjointSetElement():
    def __init__(self, x):
        self.parent = x
        self.rank = 0


class DisjointSet():
    def __init__(self, n):
        self.elems = [DisjointSetElement(n) for n in range(n)]

    def _find_set(self, x):
        if x != self.elems[x].parent:
            self.elems[x].parent = self._find_set(self.elems[x].parent)
        return self.elems[x].parent

    def same(self, x, y):
        return self._find_set(x) == self._find_set(y)

    def _link(self, x, y):
        if self.elems[x].rank > self.elems[y].rank:
            self.elems[y].parent = x
        else:
            self.elems[x].parent = y
            if self.elems[x].rank == self.elems[y].rank:
                self.elems[y].rank += 1

    def unite(self, x, y):
        self._link(self._find_set(x), self._find_set(y))


def read_inputs():
    nv, ne = [int(x) for x in input().split()]

    E = []
    for _ in range(ne):
        s, t, w = [int(x) for x in input().split()]
        E.append((w, s, t))

    return nv, E


def min_sp_tree(nv, E):
    E.sort()
    K = DisjointSet(nv)
    total = 0

    for w, s, t in E:
        if not K.same(s, t):
            K.unite(s, t)
            total += w

    return total


def main():
    nv, E = read_inputs()
    print(min_sp_tree(nv, E))


if __name__ == '__main__':
    main()
