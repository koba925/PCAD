from sys import maxsize

WHITE = 0
GRAY = 1
BLACK = 2


class Node():
    def __init__(self, key):
        self.key = key
        self.color = WHITE
        self.d = maxsize
        self.p = -1
        self.adj = []

    def __repr__(self):
        return "Node({},{},{})".format(
            self.key, self.color,
            [(a.key, w) for a, w in self.adj])


def read_inputs():
    nv, ne = [int(x) for x in input().split()]
    G = [Node(k) for k in range(nv)]
    for _ in range(ne):
        s, t, w = [int(x) for x in input().split()]
        G[s].adj.append((G[t], w))
        G[t].adj.append((G[s], w))
    return G


def weight_between(G, u, v):
    for a, w in u.adj:
        if a == v:
            print(u, v, w)
            return w


def min_sp_tree(G):

    G[0].d = 0

    while True:
        minv = maxsize
        u = None

        for v in G:
            if minv > v.d and v.color != BLACK:
                u = v
                minv = v.d

        if u is None:
            break

        u.color = BLACK
        for v in G:
            if v.color == BLACK:
                continue
            for a, w in u.adj:
                if a != v:
                    continue
                if v.d > w:
                    v.d = w
                    v.p = u
                    v.color = GRAY

    return sum([weight_between(G, v.p, v) for v in G if v.p != -1])


def main():
    G = read_inputs()
    print(min_sp_tree(G))


if __name__ == '__main__':
    main()
