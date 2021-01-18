from pprint import pprint
import copy

id_to_name = {'1': '北京',
              '10': '黑龙江',
              '11': '江苏',
              '12': '浙江',
              '13': '安徽',
              '14': '福建',
              '15': '江西',
              '16': '山东',
              '17': '河南',
              '18': '湖北',
              '19': '湖南',
              '2': '天津',
              '20': '广东',
              '21': '甘肃',
              '22': '四川',
              '23': '贵州',
              '24': '海南',
              '25': '云南',
              '26': '青海',
              '27': '陕西',
              '28': '广西',
              '29': '西藏',
              '3': '上海',
              '30': '宁夏',
              '31': '新疆',
              '32': '内蒙古',
              '33': '澳门',
              '34': '香港',
              '4': '重庆',
              '5': '河北',
              '6': '山西',
              '7': '台湾',
              '8': '辽宁',
              '9': '吉林'}

# 图节点个数
N = 34


# 根据节点id获取省份名称
def get_province_name_by_id(id):
    if id >= 1 and id <= N:
        return id_to_name[str(id)]

    return ""


# 加载地图数据，以邻接表形式保存地图信息
def load_graph(filename):
    g = [0]*34
    g.append(dict())

    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    for line in lines:
        ids = line.split(',')
        int_list = []
        for id in ids:
            int_list.append(int(id))
        g[int_list[0]] = int_list[1:]

    return g


# 保存着色过程
def save_graph(coloring_record):
    global N
    result = []
    for record in coloring_record:
        cur_coloring_result = []
        for i in range(1, N+1):
            cur_coloring_result.append((get_province_name_by_id(i), record[i]))
        result.append(cur_coloring_result)
    return result
            

    
# 获取cur节点周围可用的颜色
def get_unused_color(cur, graph, node_color):
    unused_color = set((1, 2, 3, 4))
    for node in graph[cur]:
        if (node_color[node] in unused_color):
            unused_color.remove(node_color[node])
    return list(unused_color)


# 查找下一个未被着色的节点
def find_next_node(node_color):
    for node in range(1, N+1):
        if(node_color[node] == 0):
            return node
    return -1


def coloring(cur, graph, node_color, coloring_record):
    # 记录着色过程
    coloring_record.append(copy.deepcopy(node_color))

    # 获取可用的颜色
    unused_color = get_unused_color(cur, graph, node_color)

    # 如果存在可以使用的颜色
    if(unused_color):
        # 为节点 cur 上色
        for color in unused_color:
            node_color[cur] = color
            next_node = find_next_node(node_color)
            
            if(next_node > 0):
                result = coloring(next_node, graph, node_color, coloring_record)
                # 当前着色方案可行
                if(result):
                    return True
                else:
                    continue
            # 所有节点上色完毕
            else:
                return True
        # 当前涂色方案不可行，清空颜色
        node_color[cur] = 0
    # 当前节点没有可用颜色或者当前涂色方案无解，返回False
    return False

# 算法入口
# interval用于控制记录中间着色过程的间隔，如果值为1，则记录每一次着色过程，如果值为10，则以10次迭代过程为单位记录着色过程
def start(interval):
    # 记录省份的颜色
    # 0表示无色，1、2、3、4表示4种不同的颜色
    coloring_record = []
    china_map = load_graph('data/chinamap_adj_data.txt')
    node_color = [0]*(N+1)

    if(coloring(1, china_map, node_color, coloring_record)):
        coloring_record.append(copy.deepcopy(node_color))
    else:
        print("无解")

    result = save_graph(coloring_record)

    final_result = []
    i = 1
    final_result.append(result[0])
    while(i * interval<len(result)):
        final_result.append(result[i*interval])
        i = i+1

    final_result.append(result[-1])
    return final_result


if __name__ == "__main__":
    result = start(1)
