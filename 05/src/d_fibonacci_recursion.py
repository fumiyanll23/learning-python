# find N-th Fibonacci number by recursion

def fibonacci(N: int) -> int:
    if N==1 or N == 2:
        return 1
    else:
        return fibonacci(N-1) + fibonacci(N-2)

def main():
    # input
    N = int(input())

    # compute

    # output
    print(fibonacci(N))


if __name__ == '__main__':
    main()
