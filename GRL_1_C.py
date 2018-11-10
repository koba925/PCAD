INF = 2000000000
NEG = -1
COMP = 0
CONT = 1


def read_adj_mat():
    nv, ne = [int(x) for x in input().split()]
    A = [[0 if fr == to else INF for fr in range(nv)] for to in range(nv)]
    for _ in range(ne):
        s, t, d = [int(x) for x in input().split()]
        A[s][t] = d
    return A


def step(A):
    result = COMP
    n = len(A)
    D = [fr[:] for fr in A]
    for fr in range(n):
        for to in range(n):
            here = A[fr][to]
            if fr == to or here == INF:
                continue
            for to2 in range(n):
                here2 = A[to][to2]
                if to == to2 or here2 == INF:
                    continue
                new = here + here2
                if fr == to2 and new < 0:
                    return NEG, None
                elif new < D[fr][to2]:
                    D[fr][to2] = new
                    result = CONT
    return result, D


def get_shortest_paths(A):

    while True:
        result, D = step(A)
        if result == NEG:
            return NEG, None
        elif result == COMP:
            return COMP, D
        A = D


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
    A = read_adj_mat()
    result, D = get_shortest_paths(A)
    if result == NEG:
        print("NEGATIVE CYCLE")
    else:
        print_result(D)


if __name__ == '__main__':
    main()
