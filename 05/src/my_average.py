# compute average of N items

def my_average(N: int, As: list) -> float:
    return sum(As) / N

def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute

    # output
    print(my_average(N, As))

if __name__ == '__main__':
    main()
