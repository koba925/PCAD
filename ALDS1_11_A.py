def read_adj_list(n):
    al = [None for _ in range(n + 1)]
    for _ in range(n):
        u, _, *v = (int(x) for x in input().split())
        al[u] = v
    return al


def adj_list_to_matrix(n, al):
    am = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in al[i]:
            am[i][j] = 1
    return am


def print_adj_mat(n, am):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j > 1:
                print(" ", end="")
            print(am[i][j], end="")
        print()


def main():
    n = int(input())

    adj_list = read_adj_list(n)
    adj_mat = adj_list_to_matrix(n, adj_list)
    print_adj_mat(n, adj_mat)


if __name__ == '__main__':
    main()
