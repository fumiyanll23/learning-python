# F - Bubble Sort

def bubble_sort(As: list) -> list:
    N = len(As)
    for i in range(N-1):
        for j in range(N-i-1):
            if As[j] > As[j+1]:
                As[j], As[j+1] = As[j+1], As[j]
    return As


def main():
    # input
    As = list(map(int, input().split()))

    # compute

    # output
    print(bubble_sort(As))


if __name__ == '__main__':
    main()
