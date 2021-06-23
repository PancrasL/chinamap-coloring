# python3 view.py [start_province_id] [0|1]
# 例如：
# 1. python3 view.py 1 0 表示从省份1开始着色，只显示正确的着色路径
# 2. python3 view.py 1 1 表示从省份1开始着色，显示所有的着色路径

from pyecharts.charts import Map, Geo, Timeline
from pyecharts import options as opts
import sys
import os

import coloring_algorithm as coloring


def load_data(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    data = []
    for line in lines:
        a, b = line.split(' ')
        t = tuple([a, int(b)])
        data.append(t)
    return data


def generate_map(data, i):
    map = (
        Map()
        .add("", data, "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="中国地图着色" + str(i), pos_right="center", pos_top="5%"),
            visualmap_opts=opts.VisualMapOpts(max_=4),
        )
    )
    return map

if __name__ == "__main__":
    if len(sys.argv) == 3:
        node_id = sys.argv[1]
        is_true = False if sys.argv[2] == '1' else True
        datas = coloring.start(node_id, is_true)

        timeline = Timeline()
        timeline.add_schema(play_interval='100', is_loop_play=False)
        index = 1
        for d in datas:
            timeline.add(generate_map(d, index), str(index))
            index = index + 1
        folder_path = 'output/'
        if not os.path.exists(folder_path):  #判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(folder_path)
        timeline.render(path='output/mapcoloring.html')
