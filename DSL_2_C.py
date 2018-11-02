def read_points():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = [int(x) for x in input().split()]
        points.append((x, y))
    return n, points


def pick_points(sx, tx, sy, ty, n, points):
    for i in range(n):
        if sx <= points[i][0] <= tx and \
           sy <= points[i][1] <= ty:
            print(i)
    print()


def process_queries(n, points):
    q = int(input())
    for _ in range(q):
        sx, tx, sy, ty = [int(x) for x in input().split()]
        pick_points(sx, tx, sy, ty, n, points)


def main():
    n, points = read_points()
    process_queries(n, points)


if __name__ == '__main__':
    main()
