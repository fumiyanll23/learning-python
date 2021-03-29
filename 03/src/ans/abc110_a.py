# ABC110A - Maximize the Formula

def main():
    # input
    numbers = list(map(int, input().split()))

    # compute
    numbers.sort()

    # output
    print(numbers[2]*10 + numbers[1] + numbers[0])

if __name__ == '__main__':
    main()
