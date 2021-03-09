# Python勉強会 in 数理工学生ゼミ #00

2021/03/20 (Sat.) @数理棟2F会議室

## 今回やること - Contents

- [Python](https://github.com/fumiyanll23/PythonLearning/tree/dev/00#python)

  - Pythonとは - What Is Python?

  - Pythonのインストール - Install Python

  - エイリアスの設定 - Configure Alias

- [Visual Studio Code (VSCode)](https://github.com/fumiyanll23/PythonLearning/tree/dev/00#visual-studio-code-vscode)

  - エディタとは - What Is an Editor?

  - VSCodeのインストール - Install VSCode

  - 拡張機能の設定 [Part 1] - Configure Extensions [Part 1]

  - Settings.json [Part 1]

- [Git](https://github.com/fumiyanll23/PythonLearning/tree/dev/00#git)

  - Gitとは - What Is the Git?

  - Gitのインストール - Install Git

  - Gitの設定 - Configure Git

  - 拡張機能の設定 [Part 2] - Configure Extensions [Part 2]

  - Settings.json [Part 2]

  - GitHub

  - GitHubアカウントの作成 - Create Your GitHub Account

  - RepositoryとClone - Repository and Clone

  - Stage -> Commit -> Push

- Hands On

## Python

### Pythonとは - What Is Python?

<歴史>

1989年、オランダ人の**Guido can Rossum**が開発を始め、Pythonが生まれた (リリースされたは1991年) 。
2000年にはPython 2.0 (いわゆる**2系**)が、2008年にはPython 3.0 (いわゆる**3系**) がリリースされた。
現在は**Python Software Fundation** (PSF) という団体が中心になって開発を進めている。

注) 本勉強会では3系を使用する前提で話を進める。
そのため、2系では同様の実行結果が得られない可能性があることをあらかじめ理解しておきたい。

<プログラミング言語の分類>

プログラミング言語にはインタプリタ型言語とコンパイラ型言語が存在する。
**コンパイラ型言語** (compiler language) は、プログラミング言語で書かれたソースコードを**機械語** (**マシン語**) に変換する作業 (**コンパイル**) が必要である。
**インタプリタ型言語** (interpreter language) は、コンパイラ型言語と異なりコンパイルする必要がない。
しかしながら、**実行速度が遅くなる**という欠点がある。
Pythonは後者のインタプリタ型言語に該当する。

### Pythonのインストール - Install Python

- for [Windows](https://www.python.jp/install/windows/install.html) users

- for [macOS](https://www.python.jp/install/macos/index.html) users

- for [Ubuntu](https://qiita.com/rhene/items/ff11c7850a9a7617c50f) users

### エイリアスの設定 - Configure Aliases

既存の `python` コマンドで `Python3.x.x` が起動するように**エイリアス** (alias) を設定する。

for Windows users

以下のコマンドを実行する：

```powershell
$ Set-Alias -name python -value python3
$ Set-Alias -name pip -value pip3
```

for macOS users & Ubuntu users

まず、以下のコマンドを実行し、VSCodeにて `.bashrc` を立ち上げる。

```bash
$ code ~/.bashrc .
```

次に、 `.bashrc` に以下のコードを追記する：

```.bashrc
alias python='python3'
alias pip='pip3'
```

## Visual Studio Code (VSCode)

### エディタとは - What Is an Editor?

> **エディタ** (または**エディター**、editor) は、コンピュータ上で各種のオブジェクトを編集するソフトウェア。単に**エディタ**という場合、テキストエディタを指すことがある。

(出典：[Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%87%E3%82%A3%E3%82%BF))

注) **統合開発環境** (IDE: integrated development environment) とは異なる．特に，Visual Studio Codeはエディタだが，Visual Studioは統合開発環境である．

### VSCodeのインストール - Install VSCode

[こちら](https://code.visualstudio.com/download) からそれぞれインストーラをダウンロードする．

### 拡張機能の設定 [Part 1] - Configure Extensions [Part 1]

まず、以下のコマンドを実行し、ホームディレクトリ上でVSCodeを立ち上げる：

```powershell & terminal
$ cd
$ code .
```

次に、以下の拡張機能をインストールする：

- VSCode全般

  - Bracket Lens

  - Bracket Pair Colorizer 2

  - Live Share

  - EvilInspector

- Python関連

  - Python

  - Pylance

### Settings.json [Part 1]

[こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/00/settings.json) をコピーしてVSCode内の `settings.json` に上書きする．

## Git

### Gitとは - What Is the Git?

> Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

(出典：[Git](https://git-scm.com/))

以下、著者による邦訳：

`Gitは、すべて (小さなプロジェクトから非常に大きなプロジェクトまで) を高速かつ効率的に扱うことができる、無料で利用可能な分散型バージョン管理システムである。`

### Gitのインストール - Install Git

- for [Windows](https://git-scm.com/download/win) users

  注) リンクを踏むと自動でダウンロードが始まる。

- for macOS users

  ```terminal
  $ sudo brew install git -y
  ```

- for Ubuntu users

  ```terminal
  $ sudo apt install git -y
  ```

### Gitの設定 - Configure Git

以下のコマンドを実行する：

```powershell & terminal
$ git config --global user.name "<USER NAME>"
$ git config --global user.email <EMAIL ADRESS>
```
これにより、Git使用者の名前とメールアドレスが `~/.gitconfig` に保存される。
保存した情報は以下のコマンドを実行することで確認できる：
```powershell & terminal
$ git config -l
```

### 拡張機能の設定 [Part 2] - Configure Extensions [Part 2]

以下の拡張機能を追加でインストールする：

- Git Graph

- Git History

### Settings.json [Part 2]

[こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/00/settings_git.json) をコピーしてVSCode内の `settings.json` に追記する．

### GitHub

> GitHubは、ユーザのみなさんからヒントを得て作成された開発プラットフォームです。オープンソースプロジェクトやビジネスユースまで、GitHub上にソースコードをホスティングすることで数百万人もの他の開発者と一緒にコードのレビューを行ったり、プロジェクトの管理をしながら、ソフトウェアの開発を行うことができます。

(出典：[GitHub](https://github.co.jp/))

注) Gitとは異なり、特定のサービス名である。

### GitHubアカウントの作成 - Create Your GitHub Account

[こちら](https://github.com) にて右上の `Sign up` へ進む。

### RepositoryとClone - Repository and Clone

cf. わかばちゃん

- repository

  - public, private

- clone

  - `git clone`

### Stage -> Commit -> Push

cf. わかばちゃん

- stage

  - `git stage` (?)

- commit

  - `git commit` (?)

- push

  - `git push` (?)

- コマンドはオプションで起債する (クリックすると現れるやつ)

<details>
<summary>コマンドによるGitの操作</summary>
- stage
</details>

### Hands On

[こちら](https://github.com/fumiyanll23/PythonLearning/blob/dev/00/hands-on_00.md) のページに書いてある。
