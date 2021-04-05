# ABC169B - Multiplication 2

def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    flag = True
    if 0 in As:
        prd = 0
    else:
        prd = 1
        As.sort(reverse=True)
        for i in As:
            prd *= i
            if prd > 10**18:
                flag = False
                break

    # output
    if flag:
        print(prd)
    else:
        print(-1)


if __name__ == '__main__':
    main()
