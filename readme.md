# 中国地图着色

## 文件结构

+ **coloring_algorithm.py** 地图着色算法文件，入口为coloring_algorithm.start()
+ **map_coloring.py**   地图着色前端界面文件，使用pyecharts绘制
+ **output/mapcoloring.html**   着色结果，由map_coloring.py自动生成
+ **data/chinamap_adj_data.txt**    中国地图邻接省份的简化数据（使用）
+ **data/chinamap_adj_data.json**   中国地图邻接省份的原始数据（未使用）

## 运行方法

```bash
$ pip3 install -r requirements.txt
$ python3 map_coloring.py
# 浏览器打开生成的output/mapcoloring.html文件
```
