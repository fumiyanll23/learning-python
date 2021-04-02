# find N-th Fibonacci number

import math

def my_fibonacci_recursion(N: int) -> int:
    if N == 1:
        return 1
    elif N == 2:
        return 1
    else:
        return my_fibonacci_recursion(N-1) + my_fibonacci_recursion(N-2)

def my_fibonacci_repetition(N: int) -> int:
    x, y = 1, 1

    if N == 1:
        return x
    elif N == 2:
        return y
    else:
        for _ in range(N-2):
            x, y = y, x+y
        return y

def my_fibonacci_formula(N: int) -> int: # use Binet formula

    return (((1+math.sqrt(5))/2)**N-((1-math.sqrt(5))/2)**N) / math.sqrt(5)

def main():
    # input
    N = int(input())

    # compute

    # output
    print(my_fibonacci_recursion(N))
    print(my_fibonacci_repetition(N))
    print(int(my_fibonacci_formula(N)))

if __name__ == '__main__':
    main()
