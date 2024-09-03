import json
from collections import Counter
import matplotlib.pyplot as plt
import os

folder_path = '../output/img'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 汉字字体，优先使用楷
plt.rcParams['font.family'] = 'KaiTi'

# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# 加载JSON数据
with open('../output/output.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

with open('../output/ipLocation.json', 'w', encoding='utf-8') as json_file:
    # 统计ip_location中各个地址出现的次数
    ip_locations = [item['ip_location'] for item in data if 'ip_location' in item]
    location_counts = Counter(ip_locations)
    for location, count in location_counts.items():
        json.dump(f"{location}: {count}", json_file, ensure_ascii=False, indent=4)

    # 绘制饼图
    plt.figure(figsize=(10, 8))
    plt.pie(location_counts.values(), labels=location_counts.keys(), autopct='%1.1f%%')
    plt.title('IP 地址位置分布')
    plt.savefig('../output/img/pie_iplocation.png')
