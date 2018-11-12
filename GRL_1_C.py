INF = 2000000000


def read_adj_mat():
    nv, ne = [int(x) for x in input().split()]
    A = [[0 if fr == to else INF for fr in range(nv)] for to in range(nv)]
    for _ in range(ne):
        s, t, d = [int(x) for x in input().split()]
        A[s][t] = d
    return A


def get_shortest_paths(D):
    n = len(D)
    for to in range(n):
        for fr in range(n):
            here = D[fr][to]
            if here == INF:
                continue
            for to2 in range(n):
                here2 = D[to][to2]
                if here2 == INF:
                    continue
                D[fr][to2] = min(D[fr][to2], here + here2)


def print_result(D):
    for fr in range(len(D)):
        for to in range(len(D)):
            if to != 0:
                print(" ", end="")
            if D[fr][to] == INF:
                print("INF", end="")
            else:
                print(D[fr][to], end="")
        print()


def main():
    D = read_adj_mat()
    get_shortest_paths(D)
    for d in [D[x][x] for x in range(len(D))]:
        if d < 0:
            print("NEGATIVE CYCLE")
            break
    else:
        print_result(D)


if __name__ == '__main__':
    main()
