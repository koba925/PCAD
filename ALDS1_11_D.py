def read_friends():
    n, m = [int(x) for x in input().split()]
    adj_mat = [[False] * n for _ in range(n)]

    for _ in range(m):
        s, t = [int(x) for x in input().split()]
        adj_mat[s][t] = True
        adj_mat[t][s] = True

    return n, adj_mat


def divide_group(n, adj_mat):
    group = [None] * n

    def visit(k, g):
        group[k] = g
        for t, connected in enumerate(adj_mat[k]):
            if connected and group[t] is None:
                visit(t, g)

    for k in range(n):
        if group[k] is None:
            visit(k, k)

    return group


def answer_queries(group):
    q = int(input())

    for _ in range(q):
        s, t = [int(x) for x in input().split()]
        print("yes" if group[s] == group[t] else "no")


def main():
    n, adj_mat = read_friends()
    print(adj_mat)
    group = divide_group(n, adj_mat)
    print(group)
    answer_queries(group)


if __name__ == '__main__':
    main()
