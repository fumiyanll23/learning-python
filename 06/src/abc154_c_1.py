# ABC154C - Distinct or Not

def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute

    # output
    if len(As) == len(set(As)):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
