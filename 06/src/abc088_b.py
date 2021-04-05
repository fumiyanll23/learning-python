# ABC088B - Card Game for Two

def main():
    # input
    N = int(input())
    as = list(map(int, input().split()))

    # compute
    as.sort(reverse=True)
    A, B = 0, 0
    for i in range(N):
        if i%2 == 0:
            A += as[i]
        else:
            B += as[i]

    # output
    print(A - B)


if __name__ == '__main__':
    main()
