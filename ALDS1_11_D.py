def read_friends():
    n, m = [int(x) for x in input().split()]
    adj_list = [set() for _ in range(n)]

    for _ in range(m):
        s, t = [int(x) for x in input().split()]
        adj_list[s].add(t)
        adj_list[t].add(s)

    return n, adj_list


def divide_group(n, adj_list):
    group = [None] * n

    def visit(k, g):
        S = [k]

        while S:
            k = S.pop()
            group[k] = g
            for t in adj_list[k]:
                if group[t] is None:
                    S.append(t)

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
    n, adj_list = read_friends()
    group = divide_group(n, adj_list)
    answer_queries(group)


if __name__ == '__main__':
    main()
