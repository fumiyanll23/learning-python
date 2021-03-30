# ABC176B - Multiple of 9

def main():
    # input
    N = str(input())

    # compute
    dsum = 0
    for i in range(len(N)):
        dsum += int(N[i])

    # output
    if dsum%9 == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
