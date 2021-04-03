# Python勉強会 in 数理工学生ゼミ #05

2021/04/03 (Sat.) @数理棟2F会議室

## 今回やること - Contents

- 関数 - Functions

  - 関数とは - What Is a Function?

  - 定義，引数，戻り値，呼び出し - Definitions，Arguments，Returned Values，and Call

  - ローカル変数/グローバル変数 - Local Variables/Global Variables

- 再帰 - Recursion

- Homework

## 関数 - Functions

### 関数とは - What Is a Function?

**関数** (function) とは，入力された値に対して処理を行いその結果を返すもの．
同じ処理を複数回行うときなど，関数として定義しておくことでコードが読みやすくなる．

### 定義，引数，戻り値，呼び出し - Definitions，Arguments，Returned Values，and Call

この節は [こちら](https://www.python.jp/train/function/index.html) を参照せよ．

### ローカル変数/グローバル変数 - Local Variables/Global Variables

この節は [こちら](https://www.python.jp/train/function/local_var.html) を参照せよ．

## 再帰 - Recursion

**再帰** (recursion) とは，ある手続きの中でその手続き自身を呼び出すこと．

例) 非負整数 N の階乗

```python
def factorial(N: int) -> int:
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)
```

## Homework

[こちら](https://github.com/fumiyanll23/PythonLearning/tree/main/05/homework/README.md) に書いてある宿題をやってみましょう!
