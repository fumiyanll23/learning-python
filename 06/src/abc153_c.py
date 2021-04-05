# ABC153C - Fennec vs Monster

def main():
    # input
    N, K = map(int, input().split())
    Hs = list(map(int, input().split()))

    # compute
    Hs.sort()

    # output
    if N <= K:
        print(0)
    else:
        print(sum(Hs[:N-K]))


if __name__ == '__main__':
    main()
