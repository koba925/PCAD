from sys import maxsize


class Node:
    WHITE = 0
    GRAY = 1
    BLACK = 2

    def __init__(self):
        self.adjs = []
        self.color = Node.WHITE
        self.dist = maxsize

    def __repr__(self):
        return "Node({},{},{})".format(self.adjs, self.color, self.dist)


def read_adj():
    n = int(input())
    nodes = [Node() for _ in range(n)]

    for i in range(n):
        u, _, *rest = [int(x) for x in input().split()]
        for i in range(0, len(rest) - 1, 2):
            nodes[u].adjs.append((nodes[rest[i]], rest[i+1]))

    return nodes


def shortest_path(nodes):
    nodes[0].dist = 0
    nodes[0].color = Node.GRAY

    while True:
        min_node = min(
            [n for n in nodes if n.color != Node.BLACK],
            default=None, key=lambda n: n.dist)

        if min_node is None:
            break
        min_node.color = Node.BLACK

        for adj, c in min_node.adjs:
            if min_node.dist + c < adj.dist:
                adj.dist = min_node.dist + c
                adj.color = Node.GRAY


def print_dist(nodes):
    for u, n in enumerate(nodes):
        print(u, n.dist)


def main():
    nodes = read_adj()
    shortest_path(nodes)
    print_dist(nodes)


if __name__ == '__main__':
    main()
