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


def main():
    n, q = [int(x) for x in input().split()]
    ds = DisjointSet(n)

    for _ in range(q):
        com, x, y = [int(x) for x in input().split()]
        if com == 0:
            ds.unite(x, y)
        else:
            print(1 if ds.same(x, y) else 0)


if __name__ == '__main__':
    main()
