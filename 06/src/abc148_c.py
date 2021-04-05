# ABC148C - Snack

from math import gcd

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def main():
    # input
    A, B = map(int, input().split())

    # compute

    # output
    print(lcm(A, B))


if __name__ == '__main__':
    main()
