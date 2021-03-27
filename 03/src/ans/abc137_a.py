#ABC137A - +-x

def main():
    # input
    A, B = map(int, input().split())

    # compute
    ans = [A+B, A-B, A*B]

    # output
    print(max(ans))


if __name__ == '__main__':
    main()
