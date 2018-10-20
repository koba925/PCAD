from sys import maxsize


def twos(a):
    for i in range(0, len(a) - 1, 2):
        yield (a[i], a[i + 1])


def read_adj():
    n = int(input())
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        u, _, *rest = [int(x) for x in input().split()]
        for i in range(0, len(rest) - 1, 2):
            adj_list[u].append((rest[i], rest[i + 1]))

    return n, adj_list


def shortest_path(n, adj_list):
    dist = [maxsize] * n

    def walk(u):
        for v, c in adj_list[u]:
            if dist[u] + c < dist[v]:
                dist[v] = dist[u] + c
                walk(v)

    dist[0] = 0
    walk(0)
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
