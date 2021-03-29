# ABC147A - Blackjack

def main():
    # input
    As = list(map(int, input().split()))

    # compute

    # output
    if sum(As) >= 22:
        print('bust')
    else:
        print('win')


if __name__ == '__main__':
    main()
