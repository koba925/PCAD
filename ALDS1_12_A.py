from sys import maxsize
from functools import reduce


def read_adj_mat():
    n = int(input())
    adj_mat = [None] * (n + 1)
    for i in range(1, n + 1):
        adj_mat[i] = [None] + [int(x) for x in input().split()]
    return n, adj_mat


def min_sp_tree(n, adj_mat):
    T = set([1])
    V = set(range(1, n + 1))
    mst = []

    while T != V:
        min_edge = None
        min_edge_weight = maxsize

        for p in T:
            for u in range(1, n + 1):
                w = adj_mat[p][u]
                if u in T or w < 0:
                    continue
                if w < min_edge_weight:
                    min_edge_weight = w
                    min_edge = (p, u)
        T.add(min_edge[1])
        mst.append((min_edge, min_edge_weight))

    return mst


def mst_weight(mst):
    return reduce(lambda sum, a: sum + a[1], mst, 0)


def main():
    n, adj_mat = read_adj_mat()
    mst = min_sp_tree(n, adj_mat)
    print(mst_weight(mst))


if __name__ == '__main__':
    main()
