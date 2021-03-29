# ABC137A - +-x

def main():
    # input
    A, B = map(int, input().split())

    # compute
    ABs = [A+B, A-B, A*B]

    # output
    print(max(ABs))


if __name__ == '__main__':
    main()
