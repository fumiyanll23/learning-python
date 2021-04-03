# E - Euclidean Algorithm

def gcd(As: list) -> int:
    N, M = As[0], As[1]
    while M != 0:
        N, M = M, N%M
    return N


def main():
    # input
    As = list(map(int, input().split()))

    # compute

    # output
    print(gcd(As))


if __name__ == '__main__':
    main()
