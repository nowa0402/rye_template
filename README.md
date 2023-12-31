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

### 使用フォーマッター・リンター

- Ruff
- mypy

Ruffの0.1.2よりフォーマッター機能が追加されたため
フォーマッター・リンターともにRuffに集約。

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

[tool.mypy]
strict = true

[tool.ruff]
select = [
    "F", # pyflakes
    "E", # pycodestyle
    "W", # pycodestyle warnings
    "I", # isort
]
ignore = []
line-length = 88

[tool.ruff.per-file-ignores]
# 個別設定
# __init__.pyは未使用インポートを許容
"__init__.py" = ["F401"]

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

抜けるには`deactivate`コマンド実行
※仮想環境内で有効なコマンド

## Formatter Linter

本テンプレートは以下のフォーマッター・リンターを採用している。

- [ruff](https://github.com/astral-sh/ruff)
- [mypy](https://github.com/python/mypy)

## VSCode 設定

### 拡張機能

`vscode`の拡張機能について、必須・推奨の拡張機能を記載。

#### 必須

| Name    | ID                            |
| ------- | ----------------------------- |
| Python  | `ms-python.python`            |
| Pylance | `ms-python.vscode-pylance`    |
| Ruff    | `charliermarsh.ruff`          |
| Mypy    | `ms-python.mypy-type-checker` |

#### 推奨

| Name             | ID                         |
| ---------------- | -------------------------- |
| autodocstring    | `njpwerner.autodocstring`  |
| even-better-toml | `tamasfe.even-better-toml` |

### settings.json

windowsで使用する方は

`"${workspaceFolder}/.venv/bin/{file}"`を
`"${workspaceFolder}/.venv/Scripts/{file}`に変更して使用する。

## pre-commit

pre-commitにRuffとmypyの設定を記載している。
コミット時に検証を行いたい場合は以下手順を踏むこと

### pre-commitインストール

公式参照

- [公式](https://pre-commit.com/index.html)

```bash
pip install pre-commit
```

もしくは

```bash
brew install pre-commit
```

### 初期設定

1. .pre-commit-config.yamlをプロジェクトルートに配置
2. 以下コマンド実行

```bash
pre-commit install
```

## Github Actions

`lint`と`pytest`を行うCI/CDのtemplateを用意している。

### lint.yml

以下の静的解析を行う

- ruff
- mypy
- cspell

### test.yml

`pytest`によるテストコードの自動実施
カバレッジを表示してくれる
