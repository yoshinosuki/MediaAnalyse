import wordcloud
import re
import datetime
import pandas as pd
import json
import os
folder_path = '../output/img/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 定义违禁词列表
banned_words = ['打call', 'doge', '辣眼睛', 'tv_笑哭', 'tv_色', '哦']  # 请根据需要替换这些占位符


# 定义一个函数来清洗文本
def clean_text(text):
    for banned_word in banned_words:
        pattern = re.compile(re.escape(banned_word), re.IGNORECASE)
        text = pattern.sub('', text)
        text = re.sub(r"@\S*?", "", text)
        text = re.sub(r'\[[^\]]*\]', "", text)
    return text

# 使用 pandas 的 read_json() 方法读取 JSON 文件
df = pd.read_json('../output/output.json')

# 提取特定列的值
txt = df['content']


# 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')

# 使用 str.cat() 方法将所有文本条目合并成一个字符串
txt_combined = txt.str.cat(sep=' ')

# 在生成词云之前清洗文本
txt_combined_clean = clean_text(txt_combined)
# 使用清洗后的文本生成词云
w.generate(txt_combined_clean)

# 获取当前时间
current_time = datetime.datetime.now()

# 格式化时间为字符串，例如："2024-06-02_20-56-49"
formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")

# 创建文件名
file_name = f"wordcloud_{formatted_time}.png"
# 完整的文件路径
full_file_path = os.path.join(folder_path, file_name)

# 将词云图片导出到指定的文件夹
w.to_file(full_file_path)
print('词云生成完毕！')
