from shape import Point, Segment


def main() -> None:
    q = int(input())

    for _ in range(q):
        x0, y0, x1, y1, x2, y2, x3, y3 = \
            [int(x) for x in input().split()]
        s1 = Segment(Point(x0, y0), Point(x1, y1))
        s2 = Segment(Point(x2, y2), Point(x3, y3))
        print(1 if s1.intersects(s2) else 0)


if __name__ == "__main__":
    main()
