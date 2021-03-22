# ABC195B - Many Oranges

import math

def main():
    # input
    A, B, W = map(int, input().split())

    # compute
    W *= 1000
    l = math.ceil(W/B)
    r = math.floor(W/A)

    # output

    if l > r:
        print('UNSATISFIABLE')
    else:
        print(l, r)


if __name__ == '__main__':
    main()
