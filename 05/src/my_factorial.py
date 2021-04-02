# compute factorial of n

def my_factorial(N: int) -> int:
    if N <= 0:
        return 1
    else:
        return N * my_factorial(N-1)

def main():
    # input
    N = int(input())

    # compute

    # output
    print(my_factorial(N))


if __name__ == '__main__':
    main()
