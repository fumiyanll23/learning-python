# ABC195B - Many Oranges

import math

def main():
    # input
    A, B, W = map(int, input().split())

    # compute
    W *= 1000
    lower = int(math.ceil(W/B))
    upper = int(math.floor(W/A))

    # output

    if lower > upper:
        print('UNSATISFIABLE')
    else:
        print(lower, upper)


if __name__ == '__main__':
    main()
