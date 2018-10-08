from sys import maxsize


def read_adj():
    n = int(input())
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(1, n + 1):
        u, _, *adj = [int(x) for x in input().split()]
        adj_list[u] = adj
    return n, adj_list


def shortest_paths(n, adj_list, ini_key):
    dist = [maxsize] * (n + 1)

    S = [ini_key]
    dist[ini_key] = 0

    while S != []:
        key = S.pop()
        d = dist[key] + 1
        for k in adj_list[key]:
            if d < dist[k]:
                dist[k] = d
                S.append(k)

    return dist


def print_dist(n, dist):
    for i in range(1, n + 1):
        if dist[i] == maxsize:
            print(i, -1)
        else:
            print(i, dist[i])


def main():
    n, adj_list = read_adj()
    dist = shortest_paths(n, adj_list, 1)
    print_dist(n, dist)


if __name__ == '__main__':
    main()
