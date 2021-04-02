# find maximum and minimum of given list

def max_and_min(N: int, As: list) -> list:
    max_like = -float('inf')
    min_like = float('inf')
    for i in range(N):
        if As[i] > max_like:
            max_like = As[i]
        if As[i] < min_like:
            min_like = As[i]

    return [max_like, min_like]

def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    ans_max, ans_min = max_and_min(N, As)

    # output
    print(ans_max, ans_min)

if __name__ == '__main__':
    main()
