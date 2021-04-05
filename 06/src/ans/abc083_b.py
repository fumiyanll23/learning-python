# ABC083B - Some Sums

def main():
    # input
    N, A, B = map(int, input().split())

    # compute
    cnt = 0
    for i in range(N+1):
        dsum = sum(list(map(int, str(i))))
        if A <= dsum <= B:
            cnt += i

    # output
    print(cnt)


if __name__ == '__main__':
    main()
