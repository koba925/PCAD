from typing import List
from functools import lru_cache
from sys import setrecursionlimit


def changes(amount: int, kind: int, coins: List[int]) -> int:
    
    @lru_cache(maxsize=None)
    def rec(a: int, k: int) -> int:
        # print(a, k)
        if a == 0:
            return 0
        elif a < 0 or k < 0:
            return 50001
        else:
            return min(
                rec(a - coins[k], k) + 1,
                rec(a, k - 1))

    return rec(amount, kind - 1)


def main() -> None:
    n, m = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    # print(n, m, c)

    setrecursionlimit(10000)
    print(changes(n, m, c))


main()
