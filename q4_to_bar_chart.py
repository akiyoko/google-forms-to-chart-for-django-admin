import os

from utils import draw_bar_chart

# データの起点となるセル名
CELLNAME = 'E2'
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
# 出力ファイル名
OUTPUT_FILENAME = f'{os.path.splitext(os.path.basename(__file__))[0]}.png'

if __name__ == '__main__':
    draw_bar_chart(CELLNAME, TITLE, CHOICES, OUTPUT_FILENAME)
