# Python勉強会 in 数理工学生ゼミ #01

2021/03/22 (Mon.) @情電棟2F自習室

## 今回やること - Contents

- [インタラクティブシェル - An Interactive Shell](https://github.com/fumiyanll23/PythonLearning/tree/main/01#%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%A9%E3%82%AF%E3%83%86%E3%82%A3%E3%83%96%E3%82%B7%E3%82%A7%E3%83%AB---an-interactive-shell)

  - インタラクティブシェルとは - What Is an Interactive Shell?

  - "import this"

  - 整数と実数 - Integers and Real Numbers

- [はじめてのプログラミング - Programming for the First Time](https://github.com/fumiyanll23/PythonLearning/tree/main/01#%E3%81%AF%E3%81%98%E3%82%81%E3%81%A6%E3%81%AE%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0---programming-for-the-first-time)

  - (構造化) プログラミングの3大要素 - The Largest Three Elements of (Structured) Programming

  - スニペットの設定 - Configure Snippets

  - 変数と型 - Variables and Types

  - 注釈 - Comments

  - 関数 - Functions

  - モジュールとインポート - Modules and Import

  - より良いコードを書くために - For Writing Better Codes

- [Homework](https://github.com/fumiyanll23/PythonLearning/tree/main/01#homework)

## インタラクティブシェル - An Interactive Shell

### インタラクティブシェルとは - What Is an Interactive Shell?

> **インタラクティブシェル** とは、スクリプト言語を対話的 (インタラクティブ) に使用するために使われるキャラクタベースのシェル。

(出典：[Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%A9%E3%82%AF%E3%83%86%E3%82%A3%E3%83%96%E3%82%B7%E3%82%A7%E3%83%AB#:~:text=%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%A9%E3%82%AF%E3%83%86%E3%82%A3%E3%83%96%E3%82%B7%E3%82%A7%E3%83%AB%E3%81%A8%E3%81%AF%E3%80%81%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88,%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%A8%E3%81%97%E3%81%A6%E6%8F%90%E4%BE%9B%E3%81%95%E3%82%8C%E3%82%8B%E3%80%82))

[前回](https://github.com/fumiyanll23/PythonLearning/tree/main/00#%E3%82%A8%E3%82%A4%E3%83%AA%E3%82%A2%E3%82%B9%E3%81%AE%E8%A8%AD%E5%AE%9A---configure-aliases) でエイリアスを設定しているため，以下のコマンドを実行することでPythonのインタラクティブシェルを起動することができる：

```powershell & bash
$ python
```

### "import this"

Pythonプログラマ (pythonista) を目指すにあたり，**The Zen of Python** には目を通しておきたい．
ここにはPythonを書く上での心構えが記述されている．
以下のコマンドを実行すると読むことができる：

```python
>>> import this
```

非公式ではあるが，[こちら](https://qiita.com/IshitaTakeshi/items/e4145921c8dbf7ba57ef) に邦訳したものが置いてある．

### 整数と実数 - Integers and Real Numbers

注) この節は [こちら](https://www.python.jp/train/type_and_func/float.html) を参照せよ．

表にある演算子のみならず，演算と代入を同時に行う **複合演算子** が存在する．

例) 以下の2つの式(1)，(2)は等価である：

```python
a = 0

a = a + 1 ... (1)
a += 1 ... (2)
```

## はじめてのプログラミング - Programming for the First Time

### (構造化) プログラミングの3大要素 - The Largest Three Elements of (Structured) Programming

> **構造化プログラミング** (こうぞうかプログラミング、英: structured programming) とは、コンピュータプログラム上での処理の流れを明瞭化かつ平易化するための手法である。
> 一般的には順接、分岐、反復の三つの**制御構造** (control structures) によって処理の流れを記述することであると認識されている。
> (中略)
> その実行順序を決定するものが制御構造であり、以下の三つがある。
> 1. **順次** (sequence) 部分プログラムを順々に実行する。
> 1. **選択** (selection) 条件式が導出した状態に従い、次に実行する部分プログラムを選択して分岐する。
> 1. **反復** (repetition) 条件式が導出した特定の状態の間、部分プログラムを繰り返し実行する。

(出典：[Wikipedia](https://ja.wikipedia.org/wiki/%E6%A7%8B%E9%80%A0%E5%8C%96%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0))

### スニペットの設定 - Configure Snippets

> **スニペット** (英語: snippet) とは、「断片」という意味で、再利用可能なソースコード、マシンコード、またはテキストの小さな領域を表すプログラミング用語である。
> 通常、これらはより大きなプログラミングモジュールに組み込むために正式に定義された操作ユニットである。

(出典：[Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%B9%E3%83%8B%E3%83%9A%E3%83%83%E3%83%88))

[こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/01/python.json) をコピーしてVSCode内の `python.json` に追記する．

### 変数と型 - Variables and Types

注) この節は [こちら](https://www.python.jp/train/type_and_func/variable.html) と [こちら](https://www.python.jp/train/list/index.html#Python%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E5%9E%8B) を参照せよ．

変数には **スコープ** (scope) とよばれる概念が存在する．

> プログラミングにおける **スコープ** (英: scope, 可視範囲) とは、ある変数や関数などの名前（識別子）を参照できる範囲のこと。

(出典：[Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%97))

例)

  ```python
  >>> a = 2
  >>> a
  2
  >>> b
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'b' is not defined
  ```

主な型について以下にまとめておく：

|型|名前|用途|例|
| --- | --- | --- | --- |
|bool|ブール|真理値|True, False|
|float|浮動小数点数 (FLOATing point number) |小数|3.141592|
|int|整数 (INTeger) |整数|2|
|list|配列|複数の要素|[0, 1, 'a', "b", 'foo', "bar"]|
|str|文字列 (STRing) |文字や文字列|'foo', "bar"|

オブジェクトの型を調べるには `type()` 関数を使えばよい．

例)

  ```python
  >>> test = 'abc'
  >>> type(test)
  <class 'str'>
  ```

### 注釈 - Comments

注) この節は [こちら](https://www.python.jp/train/type_and_func/comment.html) を参照せよ．

VSCodeであれば，使用言語に関わらず `Ctrl + /` でその行を注釈化 (コメントアウト) することができる．

### 関数 - Functions

注) この節は [こちら](https://www.python.jp/train/type_and_func/function.html) を参照せよ．

### モジュールとインポート - Modules and Import

注) この節は [こちら](https://www.python.jp/train/type_and_func/modules.html) を参照せよ．

主なモジュールについて以下にまとめておく：

|モジュール名|用途|
| --- | --- |
|[math](https://docs.python.org/ja/3.6/library/math.html)|数学関数|
|[Matplotlib](https://matplotlib.org/)|データの可視化|
|[NumPy](https://numpy.org/)|数値計算 (特に，ベクトルや行列の処理) |
|[pandas](https://pandas.pydata.org/)|データ構造やデータ分析|
|[random](https://docs.python.org/ja/3/library/random.html)|疑似乱数の生成|
|[SciPy](https://www.scipy.org/)|数学，科学，工学|

### より良いコードを書くために - For Writing Better Codes

Pythonには公式のコーディング規約 ([PEP8](https://pep8-ja.readthedocs.io/ja/latest/)) が存在する．
一度は目を通しておきたい．

## Homework

[こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/01/homework_01.md) に書いてある宿題をやってみましょう!
