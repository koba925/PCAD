from shape import Point, Segment


def main() -> None:
    n = int(input())

    for _ in range(n):
        x1, y1, x2, y2, x3, y3, x4, y4 = [int(x) for x in input().split()]
        s1 = Segment(Point(x1, y1), Point(x2, y2))
        s2 = Segment(Point(x3, y3), Point(x4, y4))
        print(s1.distance_with_segment(s2))


if __name__ == "__main__":
    main()
