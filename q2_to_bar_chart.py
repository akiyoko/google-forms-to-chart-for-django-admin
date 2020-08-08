import os

from utils import draw_bar_chart

# データの起点となるセル名
CELLNAME = 'C2'
# タイトル
TITLE = 'Q2．どのようなユースケースで管理サイトを使っていますか？（複数選択可）'
# 表示する選択肢
CHOICES = [
    '開発中のテストデータ投入',
    'システム利用ユーザーの情報管理',
    '本番マスタデータのメンテナンス',
]
# 出力ファイル名
OUTPUT_FILENAME = f'{os.path.splitext(os.path.basename(__file__))[0]}.png'

if __name__ == '__main__':
    draw_bar_chart(CELLNAME, TITLE, CHOICES, OUTPUT_FILENAME)
