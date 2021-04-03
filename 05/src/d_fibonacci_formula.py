# D - Fibonacci Sequence

import math

def fibonacci(N: int) -> int: # use Binet formula
    return round((((1+math.sqrt(5))/2)**N-((1-math.sqrt(5))/2)**N) / math.sqrt(5))


def main():
    # input
    N = int(input())

    # compute

    # output
    print(fibonacci(N))


if __name__ == '__main__':
    main()
