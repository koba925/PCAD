from shape import Point, Polygon


def main() -> None:
    n = int(input())
    points = []
    for _ in range(n):
        x, y = [int(x) for x in input().split()]
        points.append(Point(x, y))
    polygon = Polygon(points)

    q = int(input())
    for _ in range(q):
        x, y = [int(x) for x in input().split()]
        print(int(polygon.contains(Point(x, y))))


if __name__ == "__main__":
    main()
