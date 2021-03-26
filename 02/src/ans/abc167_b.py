# ABC167B - Easy Linear Programming

def main():
    # input
    A, B, C, K = map(int, input().split())

    # compute

    # output
    if K <= A:
        print(K)
    elif K <= A+B:
        print(A)
    else:
        print(A - (K - (A+B)))


if __name__ == '__main__':
    main()
