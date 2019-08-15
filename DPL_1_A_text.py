from typing import List


def changes(amount: int, kind: int, coins: List[int]) -> int:

    T: List[int] = [50001] * (amount + 1)
    T[0] = 0

    for k in range(kind):
        for a in range(coins[k], amount + 1):
            T[a] = min(T[a], T[a - coins[k]] + 1)

    return T[amount]


def main() -> None:
    n, m = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]

    print(changes(n, m, c))


main()
