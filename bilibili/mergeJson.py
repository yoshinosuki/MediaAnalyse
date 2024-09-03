import json
import glob
import os

folder_path = '../output'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 使用glob模块查找当前文件夹中的所有JSON文件
json_files = glob.glob('../*.json')

# 初始化一个空列表来存储所有数据
all_data = []

# 遍历文件列表，加载每个文件的内容并添加到all_data列表中
for file_name in json_files:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
        all_data.extend(data)  # 假设每个文件的内容是一个数组

# 将合并后的数据保存为一个新的JSON文件
with open('../output/output.json', 'w', encoding='utf-8') as merged_file:
    json.dump(all_data, merged_file, ensure_ascii=False, indent=4)
    # 统计JSON中有多少条数据
    num_items = len(all_data)
    print(f"所有JSON文件已合并完毕，且共有 {num_items} 条数据。")

