# ABC154C - Distinct or Not

def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    As.sort()
    for i in range(N-1):
        if As[i] == As[i+1]:
            print('NO')
            exit()

    # output
    print('YES')


if __name__ == '__main__':
    main()
