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
existing_identifiers = set()

# 遍历文件列表，加载每个文件的内容并添加到all_data列表中
for file_name in json_files:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            identifier = item.get('aweme_id')
            if identifier and identifier not in existing_identifiers:
                all_data.append(item)
                existing_identifiers.add(identifier)

# 将合并后的数据保存为一个新的JSON文件
with open('../output/combined_output.json', 'w', encoding='utf-8') as merged_file:
    json.dump(all_data, merged_file, ensure_ascii=False, indent=4)
    # 统计JSON中有多少条数据
    num_items = len(all_data)
    print(f"JSON文件中共有 {num_items} 条数据。")
    print("所有JSON文件已合并完毕。")



