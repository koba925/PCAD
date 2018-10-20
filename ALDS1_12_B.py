from sys import maxsize

WHITE = 0
GRAY = 1
BLACK = 2


def read_adj():
    n = int(input())
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        u, _, *rest = [int(x) for x in input().split()]
        for i in range(0, len(rest) - 1, 2):
            adj_list[u].append((rest[i], rest[i + 1]))

    return n, adj_list


def shortest_path(n, adj_list):
    color = [WHITE] * n
    dist = [maxsize] * n

    dist[0] = 0
    color[0] = GRAY

    while True:
        minv = maxsize
        u = -1
        for i in range(n):
            if minv > dist[i] and color[i] != BLACK:
                u = i
                minv = dist[i]

        if u == -1:
            break
        color[u] = BLACK

        for v, c in adj_list[u]:
            if dist[u] + c < dist[v]:
                dist[v] = dist[u] + c
                color[v] = GRAY

    return dist


def print_dist(dist):
    for u, d in enumerate(dist):
        print(u, d)


def main():
    n, adj_list = read_adj()
    dist = shortest_path(n, adj_list)
    print_dist(dist)


if __name__ == '__main__':
    main()
