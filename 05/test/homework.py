import math

# A - Greeting
def greeting(S: str) -> str:
    return 'hello, ' + S


# B - Average
def average(N: int, As: list) -> float:
    return sum(As) / N


# C - Max and Min
def max_and_min(N: int, As: list) -> list:
    max_like = -float('inf')
    min_like = float('inf')
    for i in range(N):
        if As[i] > max_like:
            max_like = As[i]
        if As[i] < min_like:
            min_like = As[i]
    return [max_like, min_like]


# D - Fibonacci Sequence
def fibonacci(N: int) -> int: # use Binet formula
    return round((((1+math.sqrt(5))/2)**N-((1-math.sqrt(5))/2)**N) / math.sqrt(5))


# E - Euclidean Algorithm
def gcd_and_lcm(N: int, M: int) -> list:
    prd = N * M
    while M != 0:
        N, M = M, N%M
    return [N, prd//N]


# F - Bubble Sort
def bubble_sort(N: int, As: list) -> list:
    for i in range(N-1):
        for j in range(N-i-1):
            if As[j] > As[j+1]:
                As[j], As[j+1] = As[j+1], As[j]
    return As
