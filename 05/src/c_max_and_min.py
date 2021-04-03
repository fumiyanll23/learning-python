# C - Maximum

def my_max(As: list) -> list:
    N, max_like = len(As), -float('inf')
    for i in range(N):
        if As[i] > max_like:
            max_like = As[i]
    return max_like


def main():
    # input
    As = list(map(int, input().split()))

    # compute

    # output
    print(my_max(As))


if __name__ == '__main__':
    main()
