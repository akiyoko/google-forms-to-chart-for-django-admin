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
CELL_NAME = 'F2'
# タイトル
TITLE = 'Q5．管理サイトのカスタマイズの難易度を\n「1：簡単」から「5：難しい」で表すと？'
# X軸ラベル
XLABEL = '難易度'
# 出力画像ファイル名
OUTPUT_IMAGE_NAME = f'{os.path.splitext(os.path.basename(__file__))[0]}.png'

if __name__ == '__main__':
    drawer = ChartDrawer(
        os.path.join(INPUT_DIR, INPUT_FILENAME),
        SHEET_NAME,
        CELL_NAME,
    )
    drawer.draw_histogram(
        TITLE,
        XLABEL,
        x_max=5,
        y_max=0.5,
        bins=5,
        output_image_path=os.path.join(OUTPUT_DIR, OUTPUT_IMAGE_NAME),
    )
