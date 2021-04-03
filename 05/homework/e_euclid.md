# E - Euclidean Algorithm

## 問題文

2 つの正整数 N，M が与えられる．
N と M の最大公約数 (G.C.D.：greatest common divisor) および最小公倍数 (L.C.M.：least common multiple) を返す関数 `gcd_and_lcm` を作成せよ．
ただし，最大公約数を求めるアルゴリズムには [Euclidの互除法](https://ja.wikipedia.org/wiki/%E3%83%A6%E3%83%BC%E3%82%AF%E3%83%AA%E3%83%83%E3%83%89%E3%81%AE%E4%BA%92%E9%99%A4%E6%B3%95) を用いよ．

## 制約

- N，M は正整数である．

## 入力

入力は以下の形式で標準入力から与えられる．

```
N M
```

## 出力

N と M の最大公約数および最小公倍数を出力せよ．

## 入力例1

```
12 30
```

## 出力例1

```
6 60
```

## 入力例2

```
252 105
```

## 出力例2

```
21 1260
```
