from typing import List
from sys import setrecursionlimit


def changes(amount: int, kind: int, coins: List[int]) -> int:

    min_changes = 50001

    def rec(a: int, k: int, changes: int) -> None:
        nonlocal min_changes
        # print(a, k, changes)
        if a == 0:
            min_changes = min(min_changes, changes)
            return
        elif a < 0 or k < 0:
            return
        else:
            rec(a - coins[k], k, changes + 1)
            rec(a, k - 1, changes)

    rec(amount, kind - 1, 0)
    return min_changes


def main() -> None:
    n, m = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    # print(n, m, c)

    setrecursionlimit(10000)
    print(changes(n, m, c))


main()
