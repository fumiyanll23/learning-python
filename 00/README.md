# Python勉強会 in 数理工学生ゼミ #00

2021/03/20 (Sat.) @数理棟2F会議室

## 今回やること - Contents

- [Python](https://github.com/fumiyanll23/PythonLearning/tree/main/00#python)

  - Pythonとは - What Is Python?

  - Pythonのインストール - Install Python

  - エイリアスの設定 - Configure Alias

- [Visual Studio Code (VSCode)](https://github.com/fumiyanll23/PythonLearning/tree/main/00#visual-studio-code-vscode)

  - エディタとは - What Is an Editor?

  - VSCodeのインストール - Install VSCode

  - 拡張機能の設定 [Part 1] - Configure Extensions [Part 1]

  - Settings.json [Part 1]

- [Git](https://github.com/fumiyanll23/PythonLearning/tree/main/00#git)

  - Gitとは - What Is the Git?

  - Gitのインストール - Install Git

  - Gitの設定 - Configure Git

  - 拡張機能の設定 [Part 2] - Configure Extensions [Part 2]

  - Settings.json [Part 2]

  - GitHub

  - GitHubアカウントの作成 - Create Your GitHub Account

  - リポジトリとクローン - Repository and Clone

  - プル -> ステージ -> コミット -> プッシュ - Pull -> Stage -> Commit -> Push

- [Homework](https://github.com/fumiyanll23/PythonLearning/tree/main/00#homework)

- [参考文献](https://github.com/fumiyanll23/PythonLearning/tree/main/00#%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE)

## Python

### Pythonとは - What Is Python?

- 歴史

  1989年，オランダ人の**Guido van Rossum**が開発を始め，Pythonが生まれた (リリースされたは1991年) ．
  2000年にはPython 2.0 (いわゆる**2系**)が，2008年にはPython 3.0 (いわゆる**3系**) がリリースされた．
  現在は**Python Software Fundation** (PSF) という団体が中心になって開発を進めている．

  注) 本勉強会では3系を使用する前提で話を進める．
  そのため，2系では同様の実行結果が得られない可能性があることをあらかじめ理解しておきたい．

- プログラミング言語の分類

  プログラミング言語にはインタプリタ型言語とコンパイラ型言語が存在する．
  **コンパイラ型言語** (compiled language) は，プログラミング言語で書かれたソースコードを**機械語** または **マシン語** (machine language) に変換する作業 (**コンパイル**) が必要である．
  **インタプリタ型言語** (interpreted language) は，コンパイラ型言語と異なりコンパイルする必要がない．
  しかしながら，**実行速度が遅くなる**という欠点がある．
  Pythonは後者のインタプリタ型言語に該当する．

### Pythonのインストール - Install Python

- for [Windows](https://www.python.jp/install/windows/install.html) users

- for [macOS](https://www.python.jp/install/macos/index.html) users

- for [Ubuntu](https://qiita.com/rhene/items/ff11c7850a9a7617c50f#3-ubuntu%E3%81%AE%E3%82%A2%E3%83%83%E3%83%97%E3%83%87%E3%83%BC%E3%83%88) users

### エイリアスの設定 - Configure Aliases

既存の `python` コマンドで `Python3.x.x` が起動するように**エイリアス** (alias) を設定する：

- for Windows users

  ```powershell
  $ Set-Alias -name python -value python3
  $ Set-Alias -name pip -value pip3
  ```

- for macOS or Ubuntu users

  ```bash
  $ echo -e "alias python='python3' \nalias pip='pip3'" >> .bashrc
  ```

## Visual Studio Code (VSCode)

### エディタとは - What Is an Editor?

> **エディタ** (または**エディター**、editor) は、コンピュータ上で各種のオブジェクトを編集するソフトウェア。単に**エディタ**という場合、テキストエディタを指すことがある。

(出典：[Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%87%E3%82%A3%E3%82%BF))

注) **統合開発環境** (IDE: integrated development environment) とは異なる．例えば，Visual Studio Codeはエディタだが，Visual Studioは統合開発環境である．

### VSCodeのインストール - Install VSCode

[こちら](https://code.visualstudio.com/download) からそれぞれインストーラをダウンロードし，実行する．
インストール後，ホームディレクトリ上でVSCodeを立ち上げる：

```powershell & bash
$ cd ~
$ code .
```

### 拡張機能の設定 [Part 1] - Configure Extensions [Part 1]

以下の拡張機能をインストールする：

- VSCode全般

  - Bracket Lens

  - Bracket Pair Colorizer 2

  - Live Share

  - EvilInspector

- Python関連

  - Python

  - Pylance

- Markdown関連

  - markdownlint

### Settings.json [Part 1]

[こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/00/settings.json) をコピーしてVSCode内の `settings.json` に上書きする．

## Git

### Gitとは - What Is the Git?

> Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

(出典：[Git](https://git-scm.com/))

以下，著者による邦訳：

`Gitは，すべて (小さなプロジェクトから非常に大きなプロジェクトまで) を高速かつ効率的に扱うことができる，無料で利用可能な分散型バージョン管理システムである．`

### Gitのインストール - Install Git

- for [Windows](https://git-scm.com/download/win) users

  注) リンクを踏むと自動でダウンロードが始まる．

- for macOS users

  ```bash
  $ sudo brew install git -y
  ```

- for Ubuntu users

  ```bash
  $ sudo apt install git -y
  ```

### Gitの設定 - Configure Git

```powershell & bash
$ git config --global user.name "<USER NAME>"
$ git config --global user.email <EMAIL ADRESS>
```

これにより，Git使用者の名前とメールアドレスが `~/.gitconfig` に保存される．
保存された情報は以下のコマンドを実行することで確認できる：

```powershell & bash
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

注) Gitとは異なり，GitHubは特定のサービス名である．

### GitHubアカウントの作成 - Create Your GitHub Account

[こちら](https://github.com) にて右上の `Sign up` へ進む．

### リポジトリとクローン - Repository and Clone

- **リポジトリ** (repository) ：過去の状態や更新情報などが記録されている '貯蔵庫'．
大きく分けると，以下の4種類が存在する：

  - リモート (remote)：クラウド上にあるリポジトリ，
  
  - ローカル (local)：ローカル環境 (e.g. 自身のPC) 上にあるリポジトリ，
  
  - パブリック (public)：誰でもアクセス可能な公開されているリポジトリ，
  
  - プライベート (private)：特定の人物しかアクセスできないリポジトリ．

- **クローン** (clone)：リモートリポジトリをローカルにコピーすること．
以下のコマンドを実行することでクローンできる：

  ```powershell & bash
  $ git clone <REPOSITORY URL>
  ```

### プル -> ステージ -> コミット -> プッシュ - Pull -> Stage -> Commit -> Push

- **プル** (pull)：*リモートリポジトリ* での変更を **ローカルリポジトリ** に反映させること．

- **ステージ** (stage)：作業ディレクトリから `ステージングエリア` へ変更を追加すること．

- **コミット** (commit)：`ステージングエリア` から **ローカルリポジトリ** へ変更を追加すること．

- **プッシュ** (push)：**ローカルリポジトリ** から *リモートリポジトリ* へ変更を追加すること．

実は，一連の操作は以下のコマンドでも実行できる：

```powershell & bash
$ git pull <REMOTE NAME> <BRANCH NAME>
$ git add <FILE NAME or DIRECTORY NAME>
$ git commit -m "<COMMIT MESSAGE>"
$ git push <REMOTE NAME> <BRANCH NAME>
```

### Homework

[こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/00/homework_00.md) に書いてある宿題をやってみましょう!

### 参考文献

- 湊川あい・著，DQNEO・監修，わかばちゃんと学ぶ　Git使い方入門，C&R研究所，2017．

- [Git公式ドキュメント (日本語版)](https://git-scm.com/book/ja/v2)
