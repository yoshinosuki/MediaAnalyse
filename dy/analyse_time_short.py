import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from collections import Counter
import json
import os

folder_path = '../output'
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

# 将时间戳转换为日期
dates = [datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d') for ts in timestamps]

# 统计每个日期的时间戳数量
date_counts = Counter(dates)

# 准备绘图数据
dates = list(date_counts.keys())
counts = list(date_counts.values())

# 将字符串日期转换为datetime对象
dates = [datetime.datetime.strptime(d, '%Y-%m-%d') for d in dates]

# 创建图表长度x，y轴
plt.figure(figsize=(500, 5))

# 绘制数据
plt.bar(dates, counts)

# 设置日期格式
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # 每天显示一个刻度

# 自动调整日期标签
plt.gcf().autofmt_xdate()

plt.xlabel('日期')
plt.ylabel('数量')
plt.title('每日统计')
plt.savefig('../output/bar_time_all.png')
