# find N-th Fibonacci number by repetition

def fibonacci(N: int) -> int:
    x, y = 1, 1

    for _ in range(N-2):
        x, y = y, x+y
    return y

def main():
    # input
    N = int(input())

    # compute

    # output
    print(fibonacci(N))


if __name__ == '__main__':
    main()
