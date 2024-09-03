import datetime
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
import json

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

# 获取活跃用户数据及其昵称
activeViewer = [(item['user_id'], item['nickname']) for item in data if 'user_id' in item and 'nickname' in item]

# 创建一个默认字典来存储每个用户ID的最后昵称
last_nickname = defaultdict(str)
for user_id, nickname in activeViewer:
    last_nickname[user_id] = nickname  # 这将更新为最后一次记录的昵称

# 获取活跃次数
activeViewer_counts = Counter([user_id for user_id, _ in activeViewer])
activeViewer_sec = [(item['user_id'], item['sec_uid']) for item in data if 'user_id' in item and 'sec_uid' in item]

# 按活跃次数排序
sorted_activeViewer_counts = sorted(activeViewer_counts.items(), key=lambda item: item[1], reverse=True)

# 创建一个映射，将每个用户ID映射到其对应的SecID
user_id_to_secid = {user_id: sec_uid for user_id, sec_uid in activeViewer_sec}

# 使用sorted_activeViewer_counts中的用户ID来获取对应的SecID
sorted_user_id_to_secid = {user_id: user_id_to_secid.get(user_id, 'error') for user_id, _ in sorted_activeViewer_counts}

# 将映射保存为JSON文件
with open('../output/activeViewer.json', 'w', encoding='utf-8') as json_file:
    json.dump(sorted_user_id_to_secid, json_file, ensure_ascii=False, indent=4)

print("排序后的用户ID对应的SecID已保存到json文件中。")

# 绘制前十名用户的柱形图
top_ten_activeViewers = sorted_activeViewer_counts[:10]
nicknames = [last_nickname[user_id] for user_id, _ in top_ten_activeViewers]
counts = [count for _, count in top_ten_activeViewers]

plt.figure(figsize=(10, 5))
plt.bar(nicknames, counts, color='skyblue')
plt.xlabel('用户昵称')
plt.ylabel('活跃次数')
plt.title('前十名用户活跃次数柱形图')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../output/img/bar_activeViewer_10.png')


# 绘制50用户的柱形图
top_fifty_activeViewers = sorted_activeViewer_counts[:100]
all_nicknames = [last_nickname[user_id] for user_id, _ in top_fifty_activeViewers]
all_counts = [count for _, count in top_fifty_activeViewers]

plt.figure(figsize=(15, 5))
plt.bar(all_nicknames, all_counts, color='lightgreen')
plt.xlabel('用户昵称')
plt.ylabel('活跃次数')
plt.title('前五十用户活跃次数柱形图')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('../output/img/bar_activeViewer_50.png')

