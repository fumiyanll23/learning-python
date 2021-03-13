def main():
    # input
    a, b = map(int, (input().split()))

    # compute
    sums = a + b
    diff = a - b
    prod = a * b
    div = a / b
    quot = a // b
    mod = a % b
    pow = a ** b

    # output
    print(f'{a} + {b} = {sums}')
    print(f'{a} - {b} = {diff}')
    print(f'{a} × {b} = {prod}')
    print(f'{a} ÷ {b} = {div}')
    print(f'{a} ÷ {b} = {quot}...{mod}')
    print(f'{a} ^ {b} = {pow}')


if __name__ == '__main__':
    main()
