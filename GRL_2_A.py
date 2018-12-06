from sys import maxsize
import heapq

WHITE = 0
GRAY = 1
BLACK = 2


class Node():
    def __init__(self, key):
        self.key = key
        self.color = WHITE
        self.adj = []

    def __lt__(self, other):
        return self.key < other.key

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


def min_sp_tree(G):
    heap = []
    heapq.heappush(heap, (0, G[0]))
    total = 0

    while heap != []:
        d, u = heapq.heappop(heap)
        if u.color == BLACK:
            continue
        u.color = BLACK
        total += d
        for a, w in u.adj:
            if a.color != BLACK:
                a.color = GRAY
                heapq.heappush(heap, (w, a))

    return total


def main():
    G = read_inputs()
    print(min_sp_tree(G))


if __name__ == '__main__':
    main()
