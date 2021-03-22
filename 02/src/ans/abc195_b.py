# ABC195B - Many Oranges

def main():
    # input
    A, B, W = map(int, input().split())

    # compute
    W *= 1000 # [kg] converts [g]
    flag = True

    ## find minimum
    q_min = W // B
    r_min = W % B

    if r_min == 0:
        ans_min = q_min
    elif r_min < A:
        """WRITE HERE !!!!!"""
    else:
        ans_min = q_min + 1

    ## find maximum
    # q_max = W // A
    # r_max = W % A

    # output
    if flag:
        print(q_min)
    else:
        print('UNSATISFIABLE')

if __name__ == '__main__':
    main()
