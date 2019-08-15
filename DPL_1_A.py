from typing import List
from sys import setrecursionlimit


def changes(amount: int, kind: int, coins: List[int]) -> int:

    cache: List[List[int]] = [[False] * (kind + 1) for _ in range(amount + 1)]

    def rec(a: int, k: int) -> int:
        if a < 0 or k < 0:
            return 50001
        if cache[a][k]:
            return cache[a][k]
        if a == 0:
            result = 0
        else:
            result = min(rec(a - coins[k], k) + 1, rec(a, k - 1))

        cache[a][k] = result
        return result

    return rec(amount, kind - 1)


def main() -> None:
    n, m = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]

    setrecursionlimit(10000)
    print(changes(n, m, c))


main()
