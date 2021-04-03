import math

# A - Greeting
def greeting(S: str) -> str:
    return 'hello, ' + S


# B - Average
def average(As: list) -> float:
    return sum(As) / len(As)


# C - Maximum
def my_max(As: list) -> int:
    N, max_like = len(As), -float('inf')
    for i in range(N):
        if As[i] > max_like:
            max_like = As[i]
    return max_like


# D - Fibonacci Sequence
def fibonacci(N: int) -> int: # use Binet formula
    return round((((1+math.sqrt(5))/2)**N-((1-math.sqrt(5))/2)**N) / math.sqrt(5))


# E - Euclidean Algorithm
def gcd(As: list) -> int:
    N, M = As[0], As[1]
    while M != 0:
        N, M = M, N%M
    return N


# F - Bubble Sort
def bubble_sort(As: list) -> list:
    N = len(As)
    for i in range(N-1):
        for j in range(N-i-1):
            if As[j] > As[j+1]:
                As[j], As[j+1] = As[j+1], As[j]
    return As
