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
CELL_NAME = 'B2'
# タイトル
TITLE = 'Q1．管理サイト（Django Admin）を使っていますか？'
# 表示する選択肢
CHOICES = [
    'いつも使っている',
    'たまに使っている',
    'ほとんど or 全然使っていない',
]
# 出力画像ファイル名
OUTPUT_IMAGE_NAME = f'{os.path.splitext(os.path.basename(__file__))[0]}.png'

if __name__ == '__main__':
    drawer = ChartDrawer(
        os.path.join(INPUT_DIR, INPUT_FILENAME),
        SHEET_NAME,
        CELL_NAME,
    )
    drawer.draw_pie_chart(
        TITLE,
        CHOICES,
        os.path.join(OUTPUT_DIR, OUTPUT_IMAGE_NAME),
    )
