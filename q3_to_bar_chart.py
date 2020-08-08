import os

from utils import draw_bar_chart

# データの起点となるセル名
CELLNAME = 'D2'
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
# 出力ファイル名
OUTPUT_FILENAME = f'{os.path.splitext(os.path.basename(__file__))[0]}.png'

if __name__ == '__main__':
    draw_bar_chart(CELLNAME, TITLE, CHOICES, OUTPUT_FILENAME)
