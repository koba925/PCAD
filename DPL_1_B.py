from typing import List, NamedTuple
import pprint

pp = pprint.PrettyPrinter()


class Baggage(NamedTuple):
    value: int
    weight: int


def knapsack(
    total_weight: int, n_baggages: int, baggages: List[Baggage]
) -> int:

    T: List[List[int]] = [
        [0] * (n_baggages + 1) for _ in range(total_weight + 1)
    ]

    for n in range(1, n_baggages + 1):
        for t in range(1, total_weight + 1):
            v = T[t][n - 1]
            b = baggages[n - 1]
            if t >= b.weight:
                v_use = T[t - b.weight][n - 1] + b.value
                v = max(v, v_use)
            T[t][n] = v
        # pp.pprint(T)

    return T[total_weight][n_baggages]


def main() -> None:
    N, W = [int(x) for x in input().split()]

    B: List[Baggage] = []
    for _ in range(N):
        v, w = (int(x) for x in input().split())
        B.append(Baggage(v, w))

    print(knapsack(W, N, B))


main()
