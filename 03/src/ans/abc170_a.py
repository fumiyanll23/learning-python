# ABC170A - Five Variables

def main():
    # input
    xs = list(map(int, input().split()))

    # compute
    for i in range(5):
        if(xs[i] == 0):
            print(i + 1)

    # output


if __name__ == '__main__':
    main()
