# ABLB - Integer Preference

def main():
    # input
    A, B, C, D = map(int, input().split())

    # compute

    # output
    if (B-C)*(D-A) >= 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
