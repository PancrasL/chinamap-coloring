from pyecharts.charts import Map, Geo
from pyecharts import options as opts
from pyecharts.charts import Timeline
# data=[("广东",1),("山东",1),("河南",1),("四川",1),("江苏",2),("河北",2),("湖南",2),("安徽",3),("浙江",3),("湖北",3)]

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

# 播放间隔，最小值为1
interval = 20
datas = coloring.start(interval)


timeline = Timeline()
timeline.add_schema(play_interval='100', is_loop_play=False)
index = 1
for d in datas:
    timeline.add(generate_map(d, index), str(index))
    index = index + 1

timeline.render(path='output/mapcoloring.html')
