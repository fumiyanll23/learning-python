# ABC176B - Multiple of 9

def main():
    # input


    # compute

    # output
    print(['No', 'Yes'][int(not(sum(map(int, list(input()))) % 9))])


if __name__ == '__main__':
    main()
