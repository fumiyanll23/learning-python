# Python勉強会 in 数理工学生ゼミ #00

2021/03/20 (Sat.) @数理棟2F会議室

## 今回やること - Contents

- Python

  - Pythonとは - What Is Python?

  - Pythonのインストール - Install Python

- Visual Studio Code (VSCode)

  - エディタとは - What Is an Editor?

  - VSCodeのインストール - Install VSCode

  - 拡張機能の設定 [Part 1] - Configure Extensions [Part 1]

  - Settings.json [Part 1]

- Git

  - Gitとは - What Is the Git?

  - Gitのインストール - Install Git

  - 拡張機能の設定 [Part 2] - Configure Extensions [Part 2]

  - Settings.json [Part 2]

  - GitHub

  - GitHubアカウントの作成 - Create Your GitHub Account

  - RepositoryとClone - Repository and Clone

  - Stage -> Commit -> Push

## Python

### Pythonとは - What Is Python?

- プログラミング言語として

  - インタプリタ/コンパイラ

    - 実行速度

    - メモリ

- 2系/3系

### Pythonのインストール - Install Python

- for [Windows](https://www.python.jp/install/windows/install.html) users

- for [macOS](https://www.python.jp/install/macos/index.html) users

- for [Ubuntu](https://qiita.com/rhene/items/ff11c7850a9a7617c50f) users

## Visual Studio Code (VSCode)

### エディタとは - What Is an Editor?

> **エディタ** (または**エディター**、editor) は、コンピュータ上で各種のオブジェクトを編集するソフトウェア。単に**エディタ**という場合、テキストエディタを指すことがある。

(出典：[Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%87%E3%82%A3%E3%82%BF))

注) 統合開発環境 (IDE: integrated development environment) とは異なる．特に，Visual Studio Codeはエディタだが，Visual Studioは統合開発環境である．

### VSCodeのインストール - Install VSCode

[こちら](https://code.visualstudio.com/download) からそれぞれインストーラをダウンロードする．

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

### Settings.json [Part 1]

[こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/00/settings.json) をコピーしてVSCode内の **settings.json** に上書きする．

## Git

### Gitとは - What Is the Git?

> Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

(出典：[Git](https://git-scm.com/))

以下、著者による訳：

`Gitは、すべて (小さなプロジェクトから非常に大きなプロジェクトまで) を高速かつ効率的に扱うことができる、無料で利用可能な分散型バージョン管理システムである。`

### Gitのインストール - Install Git

- for [Windows](https://git-scm.com/download/win) users

  注) リンクを踏むと自動でダウンロードが始まる。

- for macOS users

  ```terminal
  $ sudo brew install git
  ```

- for Ubuntu users

  ```terminal
  $ sudo apt install git
  ```

### 拡張機能の設定 [Part 2] - Configure Extensions [Part 2]

以下の拡張機能をインストールする：

- Git Graph

- Git History

### Settings.json [Part 2]

[こちら](https://github.com/fumiyanll23/PythonLearning/blob/main/00/settings_git.json) をコピーしてVSCode内の **settings.json** に上書きする．

### GitHub

> GitHubは、ユーザのみなさんからヒントを得て作成された開発プラットフォームです。オープンソースプロジェクトやビジネスユースまで、GitHub上にソースコードをホスティングすることで数百万人もの他の開発者と一緒にコードのレビューを行ったり、プロジェクトの管理をしながら、ソフトウェアの開発を行うことができます。

(出典：[GitHub](https://github.co.jp/))

注) Gitとは異なり、特定のサービス名である。

### GitHubアカウントの作成 - Create Your GitHub Account

[こちら](https://github.com) にて `Sign up` へ進む。

### RepositoryとClone - Repository and Clone

- repository

  - public, private

- clone

  - `git clone`

### Stage -> Commit -> Push

- stage

  - `git stage` (?)

- commit

  - `git commit` (?)

- push

  - `git push` (?)
