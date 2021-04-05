# ABC178B - Product Max

def main():
    # input
    a, b, c, d = map(int, input().split())

    # compute
    ans = [a*c, a*d, b*c, b*d]

    # output
    print(max(ans))


if __name__ == '__main__':
    main()
