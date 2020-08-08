import collections
import os

import matplotlib.pyplot as plt
import xlrd

from utils import get_column_values

# フォント
# （参考）https://qiita.com/yniji/items/3fac25c2ffa316990d0c
font = {'family': 'IPAexGothic'}

# 入出力ディレクトリ
INPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputs')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')

# タイトル
TITLE = 'Q3．どんなところに管理サイトのメリットを感じますか？（複数選択可）'
# 表示する選択肢
OUTPUT_CHOICES = [
    '設定不要ですぐに使える',
    'ほんの数行書くだけでモデルのCRUD機能が追加できる',
    '開発が捗る',
    'いろいろなユースケースで使える（多用途）',
    'カスタマイズしやすい（フックポイントが多数用意されている）',
]

if __name__ == '__main__':
    book = xlrd.open_workbook(os.path.join(INPUT_DIR, 'Django 管理サイトアンケート（回答）.xlsx'))
    sheet = book.sheet_by_name('フォームの回答 1')
    # 取得するデータの起点は「D2」
    data = get_column_values(sheet, 'D2')
    print(f'data={data}')
    # サンプル数
    sample_size = len(data)
    print(f'sample_size={sample_size}')

    # カンマ区切りで分割して2次元のリストを平坦化
    data = [value.split(', ') for value in data]
    data = sum(data, [])

    # 度数の大きい順に並べ替え
    counter = collections.Counter(data)
    ranked_data = counter.most_common()
    print(f'ranked_data={ranked_data}')
    # 表示する選択肢のみに限定
    ranked_data = [mc for mc in ranked_data if mc[0] in OUTPUT_CHOICES]
    print(f'ranked_data={ranked_data}')
    # ラベル
    labels = [x[0] for x in ranked_data]
    if len(set(data)) > len(ranked_data):
        labels += ['その他']
    print(f'labels={labels}')
    # 値
    values = [x[1] for x in ranked_data]
    if len(set(data)) > len(ranked_data):
        values += [len(data) - sum(values)]
    print(f'values={values}')
    # 合計
    total = sum(values)
    print(f'total={total}')

    # 共通初期設定
    plt.rc('font', **font)
    # キャンバス
    fig = plt.figure(figsize=(8, 8))
    # プロット領域（1x1分割の1番目に領域を配置せよという意味）
    ax = fig.add_subplot(111)
    # Y軸を上下反転する
    ax.invert_yaxis()
    # 棒グラフ
    ax.barh(
        labels,
        values,
        height=0.5,  # 棒の太さ
    )
    # グラフの右側に値を表示
    for i, value in enumerate(values):
        ax.text(value + 0.8, i, f'{value} ({(value / sample_size) * 100:.1f}%)')
    # タイトル
    ax.set_title(f'{TITLE} (N={sample_size})', size=16, pad=30)

    # 描画
    ouput_image_path = os.path.join(
        OUTPUT_DIR, f'{os.path.splitext(os.path.basename(__file__))[0]}.png')
    # bbox_inches='tight'を指定すると余白を自動で調整
    # （参考）https://www.haya-programming.com/entry/2018/10/11/030103
    plt.savefig(ouput_image_path, bbox_inches='tight')
