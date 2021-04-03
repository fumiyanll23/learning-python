# B - Average

def average(N: int, As: list) -> float:
    return sum(As) / N


def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute

    # output
    print(average(N, As))


if __name__ == '__main__':
    main()
