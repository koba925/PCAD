from shape import Point, Line, Circle


def main() -> None:
    cx, cy, r = [int(x) for x in input().split()]
    c = Circle(Point(cx, cy), r)
    q = int(input())

    for _ in range(q):
        x0, y0, x1, y1 = [int(x) for x in input().split()]
        line = Line(Point(x0, y0), Point(x1, y1))
        left, right = c.cross_point_line(line)
        print("{:.8f} {:.8f} {:.8f} {:.8f}".format(
            left.x, left.y, right.x, right.y))


if __name__ == "__main__":
    main()
