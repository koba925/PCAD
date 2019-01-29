from shape import float_equal, Point, Vector, Segment


def classify(s1: Segment, s2: Segment) -> int:
    if s1.is_parallel(s2):
        return 2
    elif s1.is_orthogonal(s2):
        return 1
    else:
        return 0


def main() -> None:
    q = int(input())
    for _ in range(q):
        s1, s2 = Segment(), Segment()
        s1.p1.x, s1.p1.y, s1.p2.x, s1.p2.y, \
            s2.p1.x, s2.p1.y, s2.p2.x, s2.p2.y = \
            [int(x) for x in input().split()]
        print(classify(s1, s2))


if __name__ == "__main__":
    main()
