# ABC174B - Distance

def main():
    # input
    N, D = map(int, input().split())
    dots = [list(map(int, input().split())) for _ in range(N)]

    # compute
    cnt = 0
    for i in range(N):
        if D**2 >= dots[i][0]**2+dots[i][1]**2:
            cnt += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
