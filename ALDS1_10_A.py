from functools import lru_cache


@lru_cache(maxsize=64)
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    print(fib(int(input())))


if __name__ == '__main__':
    main()
