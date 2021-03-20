# ABC183B - Billiards

def main():
    # input
    SX, SY, GX, GY = map(int, input().split())

    # compute

    # output
    print((SY*GX+SX*GY) / (SY+GY))


if __name__ == '__main__':
    main()
