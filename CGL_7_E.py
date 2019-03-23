from shape import Point, Line, Circle


def main() -> None:
    c1x, c1y, c1r = [int(x) for x in input().split()]
    c1 = Circle(Point(c1x, c1y), c1r)
    c2x, c2y, c2r = [int(x) for x in input().split()]
    c2 = Circle(Point(c2x, c2y), c2r)
    left, right = c1.cross_point_circle(c2)
    print("{:.8f} {:.8f} {:.8f} {:.8f}".format(
        left.x, left.y, right.x, right.y))


if __name__ == "__main__":
    main()
