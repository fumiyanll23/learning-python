def main():
    # input
    N, X, T = map(int, input().split())

    # compute
    time = N // X

    # output
    if N%X == 0:
        print(time * T)
    else:
        print((time+1) * T)


if __name__ == '__main__':
    main()
