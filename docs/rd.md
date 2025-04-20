# 要件定義

## 開発手段
- 言語は Python を使う
- UI は Tkinter を使う

## ファイル
以下のファイルをつくる。

```
coppai/
  coppai.py
  .coppaiignore
  testprompt1.md
  testprompt2.md
  folder1/
    folder1prompt1.md
  folder2/
    folder2prompt1.md
    folder2prompt2.md
  folder3/
    excluded.md
```

- `coppai.py` はソースコード本体である
- テスト用のスニペットを配置する
    - 直下には `testprompt*.md` を配置する
    - 直下のフォルダの中にあるスニペットも見ることができる。`folder*prompt*.md` として配置
    - スニペットの無視をテストするために `excluded*.md` もつくる
- `.coppaiignore` はスニペットとして扱わずに無視するファイルを指定する

## 動作と UI（ユーザーインターフェース）
- `python coppai.py` により起動する
- 起動するとウィンドウは表示せず、ポップアップメニューだけを表示する
    - ただしポップアップメニューの表示にウィンドウが必要な場合は、最小限のX,Yサイズで表示する
- ポップアップメニューには 1-項目 1-スニペット を表示する
    - スニペットは、coppai の直下および直下のフォルダ内に存在する、すべての markdown ファイルを走査して対象する
    - ただし .coppaiignore の記述を事前にチェックし、当てはまるものは無視する
- ポップアップメニュー内の項目を選ぶと、その項目に当てはまるスニペットをコピーする
    - このとき、スニペット内で変数が定義されているなら、その内容を展開してからコピーする
    - また、ポップアップメニュー内の項目を何も選ばず、キャンセルすることもできる
- 項目選択にせよ、キャンセルにせよ、いずれにしても coppai は終了する

## .coppaiignore の動作について
- 文法は glob 準拠で良い
