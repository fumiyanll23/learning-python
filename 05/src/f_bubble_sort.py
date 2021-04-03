# F - Bubble Sort

def bubble_sort(N: int, As: list) -> list:
    for i in range(N-1):
        for j in range(N-i-1):
            if As[j] > As[j+1]:
                As[j], As[j+1] = As[j+1], As[j]
            print(As)
    return As


def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute

    # output
    print(bubble_sort(N, As))


if __name__ == '__main__':
    main()
