import collections
import os
import re
from functools import reduce

import matplotlib.pyplot as plt
import xlrd
from colour import Color

# フォント
# （参考）https://qiita.com/yniji/items/3fac25c2ffa316990d0c
font = {'family': 'IPAexGothic'}

# 入出力ディレクトリ
INPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputs')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')

# 入力ファイルパス
INPUT_FILENAME = 'Django 管理サイトアンケート（回答）.xlsx'
# シート名
SHEET_NAME = 'フォームの回答 1'


def cellname_to_numbers(cellname):
    """
    セル名を行番号、列番号に変換する

    :param cellname: セル名 (e.g. 'A1')
    :return: 行番号、列番号のタプル
    """
    m = re.match(r'(\D+)(\d+)', cellname)
    if m is None:
        raise ValueError('「A1」形式で指定してください')
    # 列番号（0から始まる）
    # （参考）https://stackoverflow.com/a/12640614
    colnum = reduce(lambda x, y: x * 26 + y, [ord(c.upper()) - ord('A') for c in m.groups()[0]])
    # 行番号（0から始まる）
    rownum = int(m.groups()[1]) - 1
    return colnum, rownum


def get_column_values(sheet, cellname):
    """
    指定したセルから下方向の値を取得する

    :param sheet: xlrd.sheet.Sheetオブジェクト
    :param cellname: 開始セル名 (e.g. 'A1')
    """
    colnum, rownum = cellname_to_numbers(cellname)
    values = []
    for i in range(rownum, sheet.nrows):
        value = sheet.cell(i, colnum).value
        if value != '':
            values.append(value)
    return values


def get_gradation_colors(color_start, color_end, steps):
    """
    グラデーションの色リストを取得する

    （参考）https://github.com/vaab/colour
    （参考）https://www.tagindex.com/color/color_gradation.html

    :param color_start: 開始色 (e.g. '#5555ff')
    :param color_end: 終了色 (e.g. '#d5d5ff')
    :param steps: ステップ数
    """
    return [c.get_hex() for c in Color(color_start).range_to(Color(color_end), steps)]


def get_data_from_workbook(cellname):
    """
    ワークブックからデータを取得する

    :param cellname: 開始セル名 (e.g. 'A1')
    :return: データのリスト
    """
    book = xlrd.open_workbook(os.path.join(INPUT_DIR, INPUT_FILENAME))
    sheet = book.sheet_by_name(SHEET_NAME)
    data = get_column_values(sheet, cellname)
    return data


def data_to_labels_values(data, choices):
    """
    データを表示するラベルと値に変換する

    度数の大きい順に並べ替えた上で、「choices」で指定した値以外のものは「その他」でまとめて表示する

    :param data: データのリスト
    :return: ラベルのリストと値のリストのタプル
    """
    # 度数の大きい順に並べ替え
    counter = collections.Counter(data)
    ranked_data = counter.most_common()
    # 表示する選択肢のみに限定
    ranked_data = [mc for mc in ranked_data if mc[0] in choices]
    print(f'ranked_data={ranked_data}')
    # ラベル
    labels = [x[0] for x in ranked_data]
    if len(set(data)) > len(ranked_data):
        labels += ['その他']
    # 値
    values = [x[1] for x in ranked_data]
    if len(set(data)) > len(ranked_data):
        values += [len(data) - sum(values)]
    return labels, values


def draw_pie_chart(cellname, title, choices, output_filename):
    """
    円グラフを描画して保存する

    :param cellname: 開始セル名 (e.g. 'A1')
    :param title: タイトル
    :param choices: 表示する選択肢
    :param output_filename: 出力ファイル名
    """
    # ワークブックからデータを取得
    data = get_data_from_workbook(cellname)
    print(f'data={data}')
    # サンプル数
    sample_size = len(data)
    print(f'sample_size={sample_size}')

    # データを表示するラベルと値に変換
    labels, values = data_to_labels_values(data, choices)
    print(f'labels={labels}')
    print(f'values={values}')
    # 回答された選択肢の合計数
    total_values = sum(values)
    print(f'total_values={total_values}')

    # 共通初期設定
    plt.rc('font', **font)
    # キャンバス
    fig = plt.figure(figsize=(8, 8))
    # プロット領域（1x1分割の1番目に領域を配置せよという意味）
    ax = fig.add_subplot(111)

    # 切片の色をグラデーションに
    # （参考）https://github.com/vaab/colour
    # （参考）https://www.tagindex.com/color/color_gradation.html
    colors = get_gradation_colors('#236ab1', '#b8d5f1', len(values))
    print(colors)

    # 円グラフ
    ax.pie(
        values,
        labels=labels,
        colors=colors,
        startangle=90,  # 頂点から開始
        counterclock=False,  # 時計回り
        wedgeprops={'linewidth': 2, 'edgecolor': "white"},  # 枠線
        autopct='%.1f%%',  # パーセンテージで出力
    )
    # タイトル
    ax.set_title(f'{title} (N={sample_size})', size=16, pad=20)

    # 描画
    output_image_path = os.path.join(OUTPUT_DIR, output_filename)
    # bbox_inches='tight'を指定すると余白を自動で調整
    # （参考）https://www.haya-programming.com/entry/2018/10/11/030103
    plt.savefig(output_image_path, bbox_inches='tight')


def draw_bar_chart(cellname, title, choices, output_filename):
    """
    横棒グラフを描画して保存する

    :param cellname: 開始セル名 (e.g. 'A1')
    :param title: タイトル
    :param choices: 表示する選択肢
    :param output_filename: 出力ファイル名
    """
    # ワークブックからデータを取得
    data = get_data_from_workbook(cellname)
    print(f'data={data}')
    # サンプル数
    sample_size = len(data)
    print(f'sample_size={sample_size}')

    # カンマ区切りで分割して2次元のリストを平坦化
    data = [value.split(', ') for value in data]
    data = sum(data, [])

    # データを表示するラベルと値に変換
    labels, values = data_to_labels_values(data, choices)
    print(f'labels={labels}')
    print(f'values={values}')
    # 回答された選択肢の合計数
    total_values = sum(values)
    print(f'total_values={total_values}')

    # 共通初期設定
    plt.rc('font', **font)
    # キャンバス
    fig = plt.figure(figsize=(8, 8))
    # プロット領域（1x1分割の1番目に領域を配置せよという意味）
    ax = fig.add_subplot(111)

    # Y軸を上下反転する
    ax.invert_yaxis()
    # 横棒グラフ
    ax.barh(
        labels,
        values,
        height=0.5,  # 棒の太さ
    )
    # グラフの右側に値を表示
    for i, value in enumerate(values):
        ax.text(value + 0.8, i, f'{value} ({(value / sample_size) * 100:.1f}%)')
    # タイトル
    ax.set_title(f'{title} (N={sample_size})', size=16, pad=30)

    # 描画
    output_image_path = os.path.join(OUTPUT_DIR, output_filename)
    plt.savefig(output_image_path, bbox_inches='tight')
