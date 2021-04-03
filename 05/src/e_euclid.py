# E - Euclidean Algorithm

def gcd_and_lcm(N: int, M: int) -> list:
    prd = N * M
    while M != 0:
        N, M = M, N%M
    return [N, prd//N]


def main():
    # input
    N, M = map(int, input().split())

    # compute
    gcd, lcm = gcd_and_lcm(N, M)

    # output
    print(gcd, lcm)


if __name__ == '__main__':
    main()
