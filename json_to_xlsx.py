import os
import json
import pandas as pd

# 指定文件夹路径
folder_path = r'C:\Users\Morning\Desktop\hiwi\case_spider\case'
def transfer_all_jsonl():
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
            try:
                df = df.replace({r'\x00': ''}, regex=True)

                df.to_excel(excel_file_path, index=False, engine='openpyxl')

                print(f"Converted {jsonl_file_path} to {excel_file_path}")
            except Exception as e:
                print(e)
def transfer_single():
    import json
    import csv

    def jsonl_to_csv(input_file, output_file):
        # 读取jsonl文件并转换为字典列表
        with open(input_file, 'r', encoding='utf-8') as jsonl_file:
            records = [json.loads(line) for line in jsonl_file]

        # 如果没有记录，就结束函数
        if not records:
            print("No data found.")
            return

        # 确定所有字典中所有键的唯一集合
        fieldnames = set()
        for record in records:
            fieldnames.update(record.keys())

        # 写入csv文件
        with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for record in records:
                writer.writerow(record)

    # 示例使用
    input_file = r'C:\Users\Morning\Desktop\hiwi\case_spider\NewsQueryToExcel\content_self-driving_car_crashes.jsonl'  # JSONL文件路径
    output_file = 'output_data.csv'  # 输出的CSV文件路径
    jsonl_to_csv(input_file, output_file)
transfer_single()