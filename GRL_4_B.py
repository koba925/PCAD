class Node():
    def __init__(self, id):
        self.id = id
        self.adj = []
        self.radj = []
        self.passed = False

    def is_start(self):
        return self.radj == []

    def __repr__(self):
        return "Node({},{},{},{})".format(
            self.id, self.passed,
            [v.id for v in self.adj],
            [v.id for v in self.radj])


def read_edges(ne, V):
    for _ in range(ne):
        s, t = [int(x) for x in input().split()]
        V[s].adj.append(V[t])
        V[t].radj.append(V[s])


def sort(V):
    W = []

    def visit(v):
        S = []
        S.append(v)

        while S:
            v = S.pop()
            v.passed = True
            W.append(v)
            for a in v.adj:
                a.radj.remove(v)
                if a.is_start():
                    S.append(a)

    for v in V:
        if v.is_start() and not v.passed:
            visit(v)

    return W


def main():
    nv, ne = [int(x) for x in input().split()]
    V = [Node(id) for id in range(nv)]
    read_edges(ne, V)
    W = sort(V)
    [print(v.id) for v in W]


if __name__ == '__main__':
    main()
