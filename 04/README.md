# Python勉強会 in 数理工学生ゼミ #04

2021/04/01 (Thu.) @情電棟2Fセミナー室

## 今回やること - Contents

- 文字列 - Strings

  - 文字列とは - What Is a String?

  - 文字列の演算子 - Operators of Strings

- 文字列と数値 - Strings and Numerals

  - 文字列の数値化 - Numeralize Strings

  - 数値の文字列化 - Stringize Numerals

- メソッド - Methods

  - メソッドとは - What Is a Method?

  - メソッドと関数 - Methods and Functions

- (Appendix) AtCoderにおける "# input" の書き方 - How to Write "# input" in AtCoder

- Homework

## 文字列 - Strings

### 文字列とは - What Is a String?

注) この節は [こちら](https://www.python.jp/train/string/string.html) を参照せよ．

### 文字列の演算子 - Operators of Strings

注) この節は [こちら](https://www.python.jp/train/string/string_and_num.html) を参照せよ．

## 文字列と数値 - Strings and Numerals

注) この章は [こちら](https://www.python.jp/train/string/string.html#%E6%96%87%E5%AD%97%E3%81%A8%E6%95%B0%E5%AD%97%E3%81%AE%E3%81%A1%E3%81%8C%E3%81%84) を参照せよ．

### 文字列の数値化 - Numeralize Strings

注) この節は [こちら](https://www.python.jp/train/string/string_and_num.html#%E6%96%87%E5%AD%97%E5%88%97%E3%81%AE%E6%95%B0%E5%80%A4%E5%8C%96) を参照せよ．

### 数値の文字列化 - Stringize Numerals

注) この節は [こちら](https://www.python.jp/train/string/string_and_num.html#%E6%95%B0%E5%80%A4%E3%81%AE%E6%96%87%E5%AD%97%E5%88%97%E5%8C%96) を参照せよ．

## メソッド - Methods

### メソッドとは - What Is a Method?

注) この節は [こちら](https://www.python.jp/train/string/method.html) を参照せよ．

### メソッドと関数 - Methods and Functions

注) この節は [こちら](https://www.python.jp/train/string/method.html#%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89%E3%81%A8%E9%96%A2%E6%95%B0) を参照せよ．

## (Tips) AtCoderにおける "# input" の書き方 - How to Write "# input" in AtCoder

1. 1行に1個の値が入力されるとき

    input()関数を使うと，行ごとに入力を受け取ることができる．
    ただし，標準ではstr型になるので，適宜キャストを行う必要がある．

    例)

    入力：

    ```python
    X
    ```

    コード：

    ```python
    X = input() # type(A) is str
    X = int(input()) # type(A) is int
    ```

1. 1行に複数の値が入力されるとき

    map()関数を使うと，一斉にキャストを行うことができる．
    リストの変数名の末尾を 's' にしておくと，変数名だけでリストオブジェクトだと判別できる．

    例1)

    入力：

    ```python
    X Y Z
    ```

    コード：

    ```python
    X, Y, Z = map(int, input().split()) # type(X), type(Y), and type(Z) are the same (int)
    ```

    例2)

    問題文：

    長さ N の数列 A_i が...．

    入力：

    ```python
    N
    A_1 ... A_N
    ```

    コード：

    ```python
    N = int(input())
    As = list(map(int, input().split())) # type(As[*]) is int
    ```

1. 複数行に1個の値が入力されるとき

    例1)

    入力：

    ```python
    X
    Y
    Z
    ```

    コード：

    ```python
    X = int(input()) # type(X) is int
    Y = int(input()) # type(Y) is int
    Z = int(input()) # type(Z) is int
    ```

    例2) リストに格納したければ，for文とリスト内包表記を組み合わせるとよい．

    問題文：

    長さ N の数列 A_i が...．

    入力：

    ```python
    N
    A_1
    .
    .
    .
    A_N
    ```

    コード：

    ```python
    N = int(input())
    As = [int(input()) for _ in range(N)] # type(As[*]) is int
    ```

1. 複数行に複数個の値が入力されるとき

    2次元配列を使うとよい．

    例)

    問題文：

    N 行 M 列の行列 A_i,j が...．

    入力：

    ```python
    N M
    A_1,1 ... A_1,M
    .
    .
    .
    A_N,1 ... A_N,M
    ```

    コード：

    ```python
    N, M = map(int, input().split()) # type(N) and type(M) are the same (int)
    Ass = [list(map(int, input().split())) for _ in range(N)] # type(Ass[*][*]) is int
    ```

## Homework

[こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/01/homework_04.md) に書いてある宿題をやってみましょう!
