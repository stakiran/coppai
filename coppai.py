import os
import glob
import tkinter as tk
from tkinter import simpledialog
import pathspec
import sys
import pyperclip

# 定数
COPPAI_DIR = os.path.dirname(os.path.abspath(__file__))
COPPAIIGNORE_FILE = os.path.join(COPPAI_DIR, '.coppaiignore')

def load_ignore_patterns():
    if os.path.exists(COPPAIIGNORE_FILE):
        with open(COPPAIIGNORE_FILE, 'r', encoding='utf-8') as f:
            spec = pathspec.PathSpec.from_lines('gitwildmatch', f)
            return spec
    return None

def is_ignored(path, spec):
    if spec is None:
        return False
    rel_path = os.path.relpath(path, COPPAI_DIR)
    return spec.match_file(rel_path)

def find_snippet_files():
    spec = load_ignore_patterns()
    snippet_files = []
    # 直下のmdファイル
    for file in glob.glob(os.path.join(COPPAI_DIR, '*.md')):
        if not is_ignored(file, spec):
            snippet_files.append(file)
    # 直下のフォルダ内のmdファイル
    for folder in [f for f in os.listdir(COPPAI_DIR) if os.path.isdir(os.path.join(COPPAI_DIR, f))]:
        folder_path = os.path.join(COPPAI_DIR, folder)
        for file in glob.glob(os.path.join(folder_path, '*.md')):
            if not is_ignored(file, spec):
                snippet_files.append(file)
    return snippet_files

def load_snippet(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def expand_variables(text):
    # 現状は %cb% のみ対応
    cb_content = pyperclip.paste()
    return text.replace('%cb%', cb_content)

def show_popup_menu(snippets):
    root = tk.Tk()
    root.title("coppai - スニペット選択")
    # ウィンドウを最小化せず、適切なサイズで表示
    root.geometry('400x300+100+100')
    root.deiconify()

    def on_select(event):
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            snippet_text = snippets[index][1]
            expanded_text = expand_variables(snippet_text)
            pyperclip.copy(expanded_text)
            root.destroy()

    listbox = tk.Listbox(root, width=80, height=20)
    for i, (name, _) in enumerate(snippets):
        listbox.insert(tk.END, f"{i+1} - {name}")
    listbox.pack(fill=tk.BOTH, expand=True)
    listbox.bind('<<ListboxSelect>>', on_select)

    # キャンセル時はウィンドウを閉じる
    def on_cancel(event):
        root.destroy()
    root.bind('<Escape>', on_cancel)

    root.mainloop()

def main():
    snippet_files = find_snippet_files()
    print(f"スニペットファイル数: {len(snippet_files)}")  # 追加: スニペット数を表示
    snippets = []
    for file_path in snippet_files:
        name = os.path.splitext(os.path.basename(file_path))[0]
        content = load_snippet(file_path)
        snippets.append((name, content))

    if not snippets:
        print("スニペットが見つかりませんでした。")
        sys.exit(0)

    show_popup_menu(snippets)

if __name__ == '__main__':
    main()
