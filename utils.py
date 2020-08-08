import re
from functools import reduce

from colour import Color


def cellname_to_numbers(cellname):
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
    """指定したセルから下方向の値を取得する

    cellname: 開始セル (e.g. 'A1')
    """
    colnum, rownum = cellname_to_numbers(cellname)
    values = []
    for i in range(rownum, sheet.nrows):
        value = sheet.cell(i, colnum).value
        if value != '':
            values.append(value)
    return values


def get_gradation_colors(color_start, color_end, steps):
    """グラデーションの色リストを取得する

    （参考）https://github.com/vaab/colour
    （参考）https://www.tagindex.com/color/color_gradation.html

    color_start: 開始色 (e.g. '#5555ff')
    color_end: 終了色 (e.g. '#d5d5ff')
    steps: ステップ数
    """
    return [c.get_hex() for c in Color(color_start).range_to(Color(color_end), steps)]
