from aip import AipNlp
import pandas as pd
import time
import json
import os

folder_path = '../output/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


APP_ID = '78000517'
API_KEY = 'Gl8CVgD0RuPGsiwHr33AwYTN'
SECRET_KEY = 'Y9A1wxLlEDHAQCSzgnsPqBlX3lLUoSIh'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


# 使用 pandas 的 read_json() 方法读取 JSON 文件
df = pd.read_json('../output/output.json')

# 提取特定列的值
texts = df['content']

# 初始化一个字典来存储总的情感分数
total_scores = {'confidence': 0, 'negative_prob': 0, 'positive_prob': 0, 'sentiment': 0}

# 初始化一个列表来收集每次的情感分析结果
individual_results = []

# 循环遍历文本列表，分析每个文本的情感
for text in texts:
    # 使用百度api分析的函数
    response = client.sentimentClassify(text)
    # 检查'items'键是否存在于响应中
    if 'items' in response:
        scores = response['items'][0]  # 提取第一个元素的情感分数
        print(scores)
        # 收集每次的情感分析结果
        individual_results.append({'text': text, 'scores': scores})
        # 累加每个文本的情感分数到总分数
        for key in total_scores:
            total_scores[key] += scores.get(key, 0)
        time.sleep(1)
    else:
        individual_results.append({'text': text, 'scores': 'No sentiment scores available'})

# 计算平均情感分数
average_scores = {key: val / len(texts) for key, val in total_scores.items() if val != 0}

# 将总分数和平均分数添加到收集结果中
final_results = {
    'individual_results': individual_results,
    'total_scores': total_scores,
    'average_scores': average_scores
}

# 将结果保存到JSON文件
with open('../output/sentiment_results.json', 'w', encoding='utf-8') as f:
    json.dump(final_results, f, ensure_ascii=False, indent=4)

# 打印总的情感分数和平均情感分数
print(f"Total Scores: {total_scores}")
print(f"Average Scores: {average_scores}")
