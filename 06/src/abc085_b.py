# ABC085B - Kagami Mochi

def main():
    # input
    N = int(input())
    ds = [int(input()) for _ in range(N)]

    # compute
    cnt = [0 for _ in range(100)]
    for i in ds:
        cnt[i-1] += 1
    ans = 0
    for i in range(100):
        if cnt[i] != 0:
            ans += 1

    # output
    print(ans)


if __name__ == '__main__':
    main()
