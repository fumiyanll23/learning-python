#ABC147A - Blackjack

def main():
    # input
    A = list(map(int, input().split()))

    # compute

    # output
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")


if __name__ == '__main__':
    main()
