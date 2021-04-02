# Homework #05

1. 文字列 S が与えられる．
S の先頭に 'hello, ' を追加して得られる文字列 S' を返す関数 my_greeting.py を作成せよ．
解答例は [こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/my_greeting.py) ．

    - 制約

      - S は英文字のみからなる文字列である．

    - 入力

      入力は以下の形式で標準入力から与えられる．

      ```python
      S
      ```

    - 出力

      S' を出力せよ．

    - 入力例

      ```python
      Fumiyan
      ```

    - 出力例

      ```python
      hello, Fumiyan
      ```

1. 長さ N の数列が与えられる．
この数列の平均を，実数の範囲で求める関数 my_average.py を作成せよ．
解答例は [こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/my_average.py) ．

    - 制約

      - N は正整数である．

      - A_i は整数である．

      - -10^9 <= A_i <= 10^9

    - 入力

      入力は以下の形式で標準入力から与えられる．

      ```python
      N
      A_1 A_2 ... A_N
      ```

    - 出力

      A_1，...，A_N の平均を出力せよ．

    - 入力例

      ```python
      10
      11 7 1 -23 -49 100 4 21 -99 3
      ```

    - 出力例

      ```python
      -2.4
      ```

1. 長さ N の数列が与えられる．

    - 制約

      - N は正整数である．

      - A_i は整数である．

    - 入力

        入力は以下の形式で標準入力から与えられる．

        ```python
        N
        A_1 A_2 ... A_N
        ```

    1. この数列の最大値を求める関数 my_max.py を作成せよ．
    解答例は [こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/my_max.py) ．

        - 出力

          A_1，...，A_N の最大値を出力せよ．

        - 入力例

          ```python
          10
          3 -5 -2 7 -6 4 10 -9 1 8
          ```

        - 出力例

          ```python
          10
          ```

    1. この数列の最小値を求める関数 my_min.py を作成せよ．
    解答例は [こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/my_min.py) ．

        - 出力

          A_1，...，A_N の最小値を出力せよ．

        - 入力例

          ```python
          10
          3 -5 -2 7 -6 4 10 -9 1 8
          ```

        - 出力例

          ```python
          -9
          ```

1. 0以上の整数 N が与えられる．
N の階乗を返す関数 my_factorial.py を作成せよ．
解答例は [こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/src/my_factorial.py) ．

    - 制約

      - N は0以上の整数である．

    - 入力

      入力は以下の形式で標準入力から与えられる．

      ```python
      N
      ```

    - 出力

      N の階乗を出力せよ．

    - 入力例

      ```python
      6
      ```

    - 出力例

      ```python
      720
      ```

1. 長さ N の数列が与えられる．
この数列を昇順に並べ替える (ソートする) 関数 my_buble_sort.py を作成せよ．
ただし，並び替えのアルゴリズムには [バブルソート](https://ja.wikipedia.org/wiki/%E3%83%90%E3%83%96%E3%83%AB%E3%82%BD%E3%83%BC%E3%83%88) を用いよ．
解答例は [こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/my_sort.py) ．

    - 制約

      - N は正整数である．

      - A_i は整数である．

    - 入力

      入力は以下の形式で標準入力から与えられる．

      ```python
      N
      A_1 A_2 ... A_N
      ```

    - 出力

      A_1，A_2，...，A_N を昇順に並べ替えたリストを出力せよ．

    - 入力例

      ```python
      10
      3 5 2 7 6 4 10 9 1 8
      ```

    - 出力例

      ```python
      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      ```
