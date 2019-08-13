from shape import Point


def half_hull(P):
    S = []
    S.append(P[0])
    S.append(P[1])
    for i in range(2, n):
        while len(S) > 1:
            if (S[-1] - S[-2]).cross(P[i] - S[-1]) >= 0:
                break
            S.pop()
        S.append(P[i])
    return S

n = int(input())
P = []
for i in range(n):
    x, y = [int(x) for x in input().split()]
    P.append(Point(x, y))

A = half_hull(sorted(P, key=lambda p: (p.y, p.x)))[:-1] + \
    half_hull(sorted(P, key=lambda p: (p.y, p.x), reverse=True))[:-1]

print(len(A), *A, sep='\n')
