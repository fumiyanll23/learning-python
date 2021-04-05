# ABC181C - Collinearity

def main():
        # input
    N = int(input())
    dotss = [list(map(int, input().split())) for _ in range(N)]

    # compute
    dotss.sort()
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                dx1 = dotss[j][0] - dotss[i][0]
                dx2 = dotss[k][0] - dotss[j][0]
                dy1 = dotss[j][1] - dotss[i][1]
                dy2 = dotss[k][1] - dotss[j][1]
                if dx2*dy1 == dx1*dy2:
                    print('Yes')
                    exit()

    # output
    print('No')


if __name__ == '__main__':
        main()
