# coppai
AI 時代のコピペツール（定型文コピーツール）です。

![Image](https://github.com/user-attachments/assets/6a425071-e251-4b9a-904a-44ae8b561b7b)

# 使う

## インストール
入手

- このリポジトリを clone するか、ダウンロードしてください

要件

- Python 3.7+
- pyperclip

## 実行する
`python coppai.py` を実行します。

# 解説その1 ～概要～

## 定型文コピーツールって何？
- 定型文（スニペット）をコピーするツール
- 事前に定型文を保存しておき、かんたんに呼び出してコピーできるようにする

## 定型文として扱うもの
- 従来の定型文コピーツールは、以下のようなものを扱っていた
    - メールアドレスや住所や郵便番号
    - 「よろしくお願いいたします」など、よく使う定型句
    - よく使うコマンドライン
- coppai では、ChatGPT や OpenAI API など、LLM に渡すプロンプトやそのテンプレートを扱う

## coppai の名前について
- Copy Paste Tool With AI を略している
- Copy から cop を、Paste から pa を、AI から ai を取って、つなげた

# 解説その2 ～スニペットを登録・編集する～
- スニペット
    - markdown で書いてください
    - coppai.py と同じディレクトリか、ディレクトリ直下に置いてください
    - /
        - coppai.py
        - snippet1.md ★OK
        - folder/
            - snippet2.md ★OK
- スニペット内では変数が使えます
    - `%cb%` クリップボード内容に展開されます
    - `%getter_xxxx%` ゲッタースクリプト。xxxx.py が実行され、その内容が展開されます
- ゲッタースクリプトについて
    - now.py を参考にしてください
    - 何らかの処理をしたあと、**その結果をクリップボードに入れてください**

# 解説その3 ～coppaiが読み込むスニペットを制御する～
.coppaiignore を使ってください。

書き方は .gitignore と同じです。

# LICENSE
[MIT](LICENSE)
