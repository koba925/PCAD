class Node():
    WHITE = 0
    GRAY = 1
    BLACK = 2

    def __init__(self):
        self.u = Node.WHITE
        self.nt = 0
        self.d = 0
        self.f = 0

    def __repr__(self):
        return "Node({},{},{},{})".format(
            self.u, self.nt, self.d, self.f)


def read_adj():
    n = int(input())
    adj_mat = [[0] * (n + 1) for _ in range(n + 1)]

    for _ in range(n):
        id, _, *v = [int(x) for x in input().split()]
        for adj_id in v:
            adj_mat[id][adj_id] = 1

    return n, adj_mat


def depth_first_search(n, adj_mat):
    nodes = [Node() for _ in range(n + 1)]
    timestamp = 1

    def next(u):
        for v in range(nodes[u].nt, n + 1):
            nodes[u].nt += 1
            if adj_mat[u][v] == 1:
                return v
        return - 1

    def dfs(id):
        nonlocal adj_mat, n, nodes, timestamp

        S = []
        S.append(id)
        nodes[id].u = Node.GRAY
        nodes[id].d = timestamp
        while S != []:
            u = S[-1]
            v = next(u)
            if v != -1:
                if nodes[v].u == Node.WHITE:
                    nodes[v].u = Node.GRAY
                    timestamp += 1
                    nodes[v].d = timestamp
                    S.append(v)
            else:
                S.pop()
                nodes[u].u = Node.BLACK
                timestamp += 1
                nodes[u].f = timestamp

    for id in range(1, n + 1):
        if nodes[id].u == Node.WHITE:
            dfs(id)
            timestamp += 1

    return nodes


def print_result(n, nodes):
    for id in range(1, n + 1):
        print(id, nodes[id].d, nodes[id].f)


def main():
    n, adj_mat = read_adj()
    nodes = depth_first_search(n, adj_mat)
    print_result(n, nodes)


if __name__ == '__main__':
    main()
