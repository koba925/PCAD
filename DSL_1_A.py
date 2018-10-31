class DisjointSetElement():
    def __init__(self):
        self.parent = None
        self.anc = self

    def ancestor(self):
        s = self.anc
        while s.parent is not None:
            s = s.parent
        self.anc = s
        return s

    def unite(self, y):
        ax = self.ancestor()
        ay = y.ancestor()
        if ax is not ay:
            ax.parent = ay
            ax.anc = ay.anc

    def same(self, y):
        return self.ancestor() is y.ancestor()


def main():
    n, q = [int(x) for x in input().split()]
    elems = [DisjointSetElement() for _ in range(n)]

    for _ in range(q):
        com, x, y = [int(x) for x in input().split()]
        if com == 0:
            elems[x].unite(elems[y])
        else:
            print(1 if elems[x].same(elems[y]) else 0)


if __name__ == '__main__':
    main()
