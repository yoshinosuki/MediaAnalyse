import datetime
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
import json
import os

folder_path = '../output/time'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

folder_path1 = '../output/img'
if not os.path.exists(folder_path1):
    os.makedirs(folder_path1)

# 汉字字体，优先使用楷
plt.rcParams['font.family'] = 'KaiTi'

# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# 加载JSON数据
with open('../output/output.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 获取活跃用户数据及其昵称
popularVideo = [(item['title'], item['video_id'], item['liked_count'], item['video_danmaku'], item['video_comment'], item['video_play_count']) for item in data if 'title' in item and 'video_id' in item and 'liked_count' in item and 'video_danmaku' in item and 'video_comment' in item and 'video_play_count' in item]

videoData = []  # 创建一个空列表来存储所有视频的数据

for title, video_id, liked_count, video_danmaku, video_comment, video_play_count in popularVideo:
    # 确保将字符串转换为整数
    liked_count = int(liked_count)
    video_danmaku = int(video_danmaku)
    video_comment = int(video_comment)
    video_play_count = int(video_play_count)

    # 计算视频热度得分
    videoScore = 0.4 * liked_count + 0.3 * video_danmaku + 0.2 * video_comment + 0.1 * video_play_count

    # 创建一个字典来存储标题和热度得分
    videoInfo = {
        'title': title,
        'videoScore': videoScore
    }

    # 将字典添加到列表中
    videoData.append(videoInfo)

# 根据视频热度得分对 videoData 列表进行降序排序
sorted_videoData = sorted(videoData, key=lambda x: x['videoScore'], reverse=True)

# 循环结束后，将所有视频数据写入JSON文件
with open('../output/videoPopularity.json', 'w', encoding='utf-8') as json_file:
    json.dump(sorted_videoData, json_file, ensure_ascii=False, indent=4)

# 假设 videoData 是一个包含多个字典的列表，每个字典都有 'title' 和 'videoScore' 键
top_ten_videos = sorted_videoData[:12]
names = [item['title'][:8] for item in top_ten_videos]  # 提取标题的前7个字符
counts = [item['videoScore'] for item in top_ten_videos]  # 提取视频热度得分
plt.figure(figsize=(10, 7))
plt.bar(names, counts, color='skyblue')
plt.xlabel('视频标题')
plt.ylabel('热度')
plt.title('前十名视频受欢迎度得分柱形图')
plt.xticks(rotation=20)
plt.savefig('../output/img/bar_videoPopularity_10.png')
print("受欢迎的视频分析完毕！")
