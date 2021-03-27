# ABC087B - Coins

def main():
    # input
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())

    # compute
    cnt = 0
    for i in range(A+1):
        for j in range(B+1):
            for k in range(C+1):
                if 500*i+100*j+50*k == X:
                    cnt += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
