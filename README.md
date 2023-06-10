# rye VSCode Settings Template

`rye + vscode` の設定テンプレート

## 使用方法

### 前提

以下がインストール済

- [Visual Studio Code](https://code.visualstudio.com/)
- [rye](https://github.com/mitsuhiko/rye)

`rye`のインストールは以下参照

- [公式ドキュメント参照](https://rye-up.com/)
- [GitHub](https://github.com/mitsuhiko/rye)

### プロジェクト立ち上げ

テンプレートをプロジェクト配下に配置

```bash
# 必須テンプレート一覧
{project_root}
    ├── .gitignore
    ├── .python-version
    ├── .vscode
    │   └── settings.json
    └── pyproject.toml
```

`pyproject.toml`の編集を行う。
以下該当項目を列挙

```toml
[project]
name = "{プロジェクト名記載}"
description = "{説明追加}"
authors = ["{必要であれば記載}"]


[tool.black]
# 改行文字数設定
line_length = 80

[tool.flake8]
# blackの設定に合わせる
max-line-length = 80
# 警告無視の一覧は必要に応じて追加
extend-ignore = ["E203", "W503"]

[tool.mypy]
# プロジェクト毎に適切な設定を行う

```

準備ができたら以下コマンド実行

```bash
# pythonバージョンを変更する場合実行
# .python-versionのpythonバージョンを変更できる
$ rye pin 3.11

# .venv requirements-dev.lock requirements.lockが作成される
$ rye sync

# .venv 仮想環境
# requirements-dev.lock 開発用ライブラリロックファイル
# requirements.lock 本番用ライブラリロックファイル
```

### 仮想環境

接続は以下コマンド実行

#### linux

`. .venv/bin/activate`

#### windows

`.venv\Scripts\activate`

抜けるには`deactivate`コマンド※実行
※仮想環境内で有効なコマンド

## 開発用パッケージ

### formatter

- black
- isort
- flake8
- mypy
- pyproject-flake8

`pyproject-flake8`は`flake8`が`pyproject.toml`の設定を反映できないため導入している
`pyproject-flake8`のコマンドは`pflake8`

## VSCode 設定

### 推奨の拡張機能

| Name             | ID                         |
| ---------------- | -------------------------- |
| Python           | `ms-python.python`         |
| Pylance          | `ms-python.vscode-pylance` |
| isort            | `ms-python.isort`          |
| autodocstring    | `njpwerner.autodocstring`  |
| even-better-toml | `tamasfe.even-better-toml` |
