def main():
    # input
    A, B, W = map(int, input().split())

    # compute
    W *= 1000 # [kg] converts [g]

    ## find minimum
    diff = W - (W//B)*B

    # output

if __name__ == '__main__':
    main()
