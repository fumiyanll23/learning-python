# B - Average

def average(As: list) -> float:
    return sum(As) / len(As)


def main():
    # input
    As = list(map(int, input().split()))

    # compute

    # output
    print(average(As))


if __name__ == '__main__':
    main()
