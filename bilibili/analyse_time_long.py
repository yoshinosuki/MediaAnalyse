import datetime
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
import json
import os

folder_path = '../output/time'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 汉字字体，优先使用楷
plt.rcParams['font.family'] = 'KaiTi'

# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# 加载JSON数据
with open('../output/output.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 统计ip_location中各个地址出现的次数
timestamps = [item['create_time'] for item in data if 'create_time' in item]
with open('../output/activeTime.json', 'w', encoding='utf-8') as json_file:
    # 将时间戳转换为日期，并按月份分组
    monthly_data = defaultdict(list)
    for ts in timestamps:
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        month = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m')
        monthly_data[month].append(date)

    # 为每个月生成图表
    for month, dates in monthly_data.items():
        # 统计每个日期的时间戳
        date_counts = Counter(dates)
        json.dump(date_counts, json_file, ensure_ascii=False, indent=4)

        # 获取日期和计数
        dates = list(date_counts.keys())
        values = list(date_counts.values())

        # 创建图表长度x，y轴
        plt.figure(figsize=(10, 5))
        # 对日期进行排序
        sorted_dates = sorted(dates)
        plt.bar(sorted_dates, values)
        plt.xlabel('日期')
        plt.ylabel('计数')
        plt.xticks(rotation=90)  # 旋转x轴标签以便阅读
        plt.title(f'每日统计\n{month}')
        # 自动调整日期标签
        plt.gcf().autofmt_xdate()

        # 保存图表
        plt.savefig(f'../output/time/bar_time_{month}.png')
        plt.close()  # 关闭图表以释放内存

print('活跃时间分析完毕')



