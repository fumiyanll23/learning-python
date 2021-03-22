def main():
    # input
    N = int(input())

    # compute

    # output
    if N%10 == 3:
        print('bon')
    elif (N%10 == 0) or (N%10 == 1) or (N%10 == 6) or (N%10 == 8):
        print('pon')
    else:
        print('hon')


if __name__ == '__main__':
    main()
