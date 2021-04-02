# find minimum of given list

def my_min(N: int, As: list) -> int:
    min_like = float('inf')
    for i in range(N):
        if As[i] < min_like:
            min_like = As[i]

    return min_like

def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute

    # output
    print(my_min(N, As))

if __name__ == '__main__':
    main()
