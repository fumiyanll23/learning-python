# ABC159A - The Number of Even Pairs

def main():
    # input
    N, M = map(int, input().split())

    # compute
    all = (N+M) * (N+M-1) // 2
    odd = N * M

    # output
    print(all - odd)


if __name__ == '__main__':
    main()
