# ABC167A - Registration

def main():
    # input
    S = str(input())
    T = str(input())

    # compute
    flag = True
    for i in range(len(S)):
        if S[i] != T[i]:
            flag = False

    # output
    if flag:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
