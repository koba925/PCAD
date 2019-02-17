from shape import Point, Line


def main() -> None:
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    l = Line(p1, p2)

    q = int(input())

    for _ in range(q):
        x, y = [int(x) for x in input().split()]
        p = Point(x, y)
        a = l.reflection(p)
        print(a.x, a.y)


if __name__ == "__main__":
    main()
