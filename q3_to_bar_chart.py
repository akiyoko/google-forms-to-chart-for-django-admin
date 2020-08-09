import os

from utils import ChartDrawer

# 入出力ディレクトリ
INPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputs')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')
# 入力ファイル名
INPUT_FILENAME = 'Django 管理サイトアンケート（回答）.xlsx'
# シート名
SHEET_NAME = 'フォームの回答 1'
# データの起点となるセル名
CELL_NAME = 'D2'
# タイトル
TITLE = 'Q3．どんなところに管理サイトのメリットを感じますか？（複数選択可）'
# 表示する選択肢
CHOICES = [
    '設定不要ですぐに使える',
    'ほんの数行書くだけでモデルのCRUD機能が追加できる',
    '開発が捗る',
    'いろいろなユースケースで使える（多用途）',
    'カスタマイズしやすい（フックポイントが多数用意されている）',
]
# 出力画像ファイル名
OUTPUT_IMAGE_NAME = f'{os.path.splitext(os.path.basename(__file__))[0]}.png'

if __name__ == '__main__':
    drawer = ChartDrawer(
        os.path.join(INPUT_DIR, INPUT_FILENAME),
        SHEET_NAME,
        CELL_NAME,
    )
    drawer.draw_bar_chart(
        TITLE,
        CHOICES,
        os.path.join(OUTPUT_DIR, OUTPUT_IMAGE_NAME),
    )
