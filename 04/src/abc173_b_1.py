# ABC173B - Judge Status Summary

def main():
    # input
    N = int(input())

    # compute

    # output
    print((lambda s: '\n'.join(f'{r} x {s.count(r)}' for r in ['AC', 'WA', 'TLE', 'RE']))([input() for _ in range(N)]))


if __name__ == '__main__':
    main()
