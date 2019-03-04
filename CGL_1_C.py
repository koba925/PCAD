from shape import Point, Segment


def main() -> None:
    x0, y0, x1, y1 = [int(x) for x in input().split()]
    s = Segment(Point(x0, y0), Point(x1, y1))
    q = int(input())

    for _ in range(q):
        x2, y2 = [int(x) for x in input().split()]
        print(Point(x2, y2).location(s).name)


if __name__ == "__main__":
    main()
