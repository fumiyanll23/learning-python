# ABC081B - Shift only

def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    cnts = [0 for _ in range(N)]
    for i in range(N):
        while As[i]%2 == 0:
            As[i] //= 2
            cnts[i] += 1

    # output
    print(min(cnts))


if __name__ == '__main__':
    main()
