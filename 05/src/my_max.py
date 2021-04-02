# find maximum of given list

def my_max(N: int, As: list) -> int:
    max_like = -float('inf')
    for i in range(N):
        if As[i] > max_like:
            max_like = As[i]

    return max_like

def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute

    # output
    print(my_max(N, As))

if __name__ == '__main__':
    main()
