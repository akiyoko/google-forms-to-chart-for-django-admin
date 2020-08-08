import os

from utils import draw_pie_chart

# データの起点となるセル名
CELLNAME = 'B2'
# タイトル
TITLE = 'Q1．管理サイト（Django Admin）を使っていますか？'
# 表示する選択肢
CHOICES = [
    'いつも使っている',
    'たまに使っている',
    'ほとんど or 全然使っていない',
]
# 出力ファイル名
OUTPUT_FILENAME = f'{os.path.splitext(os.path.basename(__file__))[0]}.png'

if __name__ == '__main__':
    draw_pie_chart(CELLNAME, TITLE, CHOICES, OUTPUT_FILENAME)
