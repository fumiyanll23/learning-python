# ABC173B - Judge Status Summary

def main():
    # input
    N = int(input())
    Ss = []
    for _ in range(N):
        Ss.append(str(input()))

    # compute
    cnts = [0, 0, 0, 0]
    rslts = ['AC', 'WA', 'TLE', 'RE']

    for i in range(N):
        if Ss[i] == rslts[0]:
            cnts[0] += 1
        elif Ss[i] == rslts[1]:
            cnts[1] += 1
        elif Ss[i] == rslts[2]:
            cnts[2] += 1
        else:
            cnts[3] += 1

    # output
    for i in range(4):
        print(rslts[i], 'x', cnts[i])


if __name__ == '__main__':
    main()
