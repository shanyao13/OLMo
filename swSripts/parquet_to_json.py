import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

def convert_file(parquet_path, json_path):
    try:
        # 读取parquet文件
        df = pd.read_parquet(parquet_path)
        # 转换为json并保存
        df.to_json(json_path, orient="records", lines=True, force_ascii=False)
        print(f"转换成功：'{parquet_path}' -> '{json_path}'")
    except Exception as e:
        print(f"转换失败：'{parquet_path}'，错误：{e}")

def parquet_to_json(input_dir, output_dir, max_workers=4):
    # 检查输入目录是否存在
    if not os.path.isdir(input_dir):
        print(f"输入目录 '{input_dir}' 不存在，请检查路径。")
        return

    # 创建输出目录（如果不存在）
    os.makedirs(output_dir, exist_ok=True)

    # 获取所有parquet文件列表
    parquet_files = [f for f in os.listdir(input_dir) if f.endswith(".parquet")]

    # 使用线程池加速文件转换
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for file_name in parquet_files:
            parquet_path = os.path.join(input_dir, file_name)
            json_path = os.path.join(output_dir, file_name.replace(".parquet", ".json"))
            # 提交转换任务
            futures.append(executor.submit(convert_file, parquet_path, json_path))

        # 等待所有任务完成
        for future in futures:
            future.result()

if __name__ == "__main__":
    input_dir = input("请输入Parquet文件所在目录：")
    output_dir = input("请输入JSON文件保存目录：")
    max_workers = int(input("请输入并发线程数（建议为CPU核心数）："))
    parquet_to_json(input_dir, output_dir, max_workers)
