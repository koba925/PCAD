from sys import maxsize
from functools import reduce

WHITE = 0
GRAY = 1
BLACK = 2


def read_adj_mat():
    n = int(input())
    M = []
    for _ in range(n):
        M.append([maxsize if x == "-1" else int(x)
                  for x
                  in input().split()])
    return n, M


def min_sp_tree(n, M):
    d = [maxsize] * n
    p = [-1] * n
    color = [WHITE] * n

    d[0] = 0

    while True:
        minv = maxsize
        u = -1

        for i in range(n):
            if minv > d[i] and color[i] != BLACK:
                u = i
                minv = d[i]

        if u == -1:
            break

        color[u] = BLACK
        for v in range(n):
            if color[v] != BLACK and M[u][v] != maxsize:
                if d[v] > M[u][v]:
                    d[v] = M[u][v]
                    p[v] = u
                    color[v] = GRAY

    return sum([M[i][p[i]] for i in range(n) if p[i] != -1])


def main():
    n, M = read_adj_mat()
    print(min_sp_tree(n, M))


if __name__ == '__main__':
    main()
