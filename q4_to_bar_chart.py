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
CELL_NAME = 'E2'
# タイトル
TITLE = 'Q4．管理サイトのデメリットを挙げるとすればどんなものがありますか？（複数選択可）'
# 表示する選択肢
CHOICES = [
    '仕様を把握するのにひと苦労',
    '簡単にカスタマイズできるかどうかのジャッジにノウハウや調査が必要',
    'ある程度以上のカスタマイズになると難易度が上がる',
    'テストやデバッグがしづらい',
    'コードが断片化しやすい（保守が大変になりがち）',
    '画面のスタイルを変えるのが大変',
    '日本語の情報が少ない',
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
