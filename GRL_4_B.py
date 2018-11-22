class Node():
    def __init__(self, id):
        self.id = id
        self.adj = []
        self.passed = False

    def __repr__(self):
        return "Node({},{})".format(
            self.id,
            [v.id for v in self.adj])


def read_edges(ne, V):
    for _ in range(ne):
        s, t = [int(x) for x in input().split()]
        V[s].adj.append(V[t])


def is_start(V, node):
    for v in V:
        if node in v.adj:
            return False
    return True


def is_last_branch(V, node):
    for v in V:
        if node in v.adj and not v.passed:
            return False
    return True


def sort(V):
    W = []

    def rec(v):
        S = []
        S.append(v)

        while S:
            v = S.pop()
            v.passed = True
            W.append(v)
            for a in v.adj:
                if is_last_branch(V, a):
                    S.append(a)

    for v in V:
        if is_start(V, v):
            rec(v)

    return W


def main():
    nv, ne = [int(x) for x in input().split()]
    V = [Node(id) for id in range(nv)]
    read_edges(ne, V)
    W = sort(V)
    [print(v.id) for v in W]


if __name__ == '__main__':
    main()
