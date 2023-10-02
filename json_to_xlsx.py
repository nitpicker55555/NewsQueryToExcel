import os
import json
import pandas as pd

# 指定文件夹路径
folder_path = './case/'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查文件是否为JSONL文件
    if filename.endswith('.jsonl'):
        print(filename)
        # 拼接完整的文件路径
        jsonl_file_path = os.path.join(folder_path, filename)

        # 读取JSONL文件
        with open(jsonl_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            data = [json.loads(line) for line in lines]

        # 将数据转换为DataFrame
        df = pd.DataFrame(data)

        # 定义输出Excel文件的路径
        excel_file_path = os.path.join(folder_path, filename.replace('.jsonl', '.xlsx'))

        # 将DataFrame保存为Excel文件
        df.to_excel(excel_file_path, index=False, engine='openpyxl')

        print(f"Converted {jsonl_file_path} to {excel_file_path}")
