import matplotlib.pyplot as plt
import os
import json

folder_path = '../output'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

with open('../output/sentiment_results.json', 'r', encoding='utf-8') as file:
    sentiment_data = json.load(file)

# 提取情感分数
confidence = sentiment_data['average_scores']["confidence"]
negative_prob = sentiment_data['average_scores']["negative_prob"]
positive_prob = sentiment_data['average_scores']["positive_prob"]

# 创建柱状图
plt.figure(figsize=(8, 6))
plt.bar(["Negative", "Positive"], [negative_prob, positive_prob], color=["red", "green"])
plt.xlabel("Sentiment")
plt.ylabel("Probability")
plt.title("Sentiment Analysis")
plt.ylim(0, 1)  # 设置 y 轴范围为 [0, 1]

# 显示情感分数
plt.text(0, negative_prob + 0.05, f"Negative: {negative_prob:.2f}", ha="center", va="bottom")
plt.text(1, positive_prob + 0.05, f"Positive: {positive_prob:.2f}", ha="center", va="bottom")

# 保存图表（可选）
plt.savefig("../output/bar_sentiment_analysis.png")

