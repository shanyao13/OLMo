"""从dolma_v1_7/目录下各自采样给定大小总量的.json.gz文件, 并将其移动到给定的目录下"""

import os
import shutil
import random

# 定义目录X和目录Y的路径i
directory_X = "/mnt/zzb/peixunban/zzb6/home/sfx/raw/dolma_v1_7/"
directory_Y = "/mnt/zzb/peixunban/zzb6/data/swZheng/dataSet/selected/selectedFromDolma/"

sample_sizes = [3, 10, 7, 50, 3, 10, 3, 3, 8, 15, 30, 90, 10, 25, 6, 20]
folders = ["AlgebraicStack",
           "Arxiv",
           "Books",
           "C4",
           "CC_head",
           "CC_news_head",
           "CC_news_middle",
           "CC_news_tail",
           "OpenWebMath",
           "pes2o",
           "Reddit",
           "RefinedWeb",
           "StackExchange",
           "StarCoder",
           "tulu_flan",
           "wiki"]

# """也可以按比例采样"""
# sample_ratio = 0.1
# total_sizes = []
# # 遍历目录X下的文件夹
# for folder_name in os.listdir(directory_X):
#     folder_path = os.path.join(directory_X, folder_name)
#     if os.path.isdir(folder_path):
#         documents_folder = os.path.join(folder_path, "documents")
#         if os.path.exists(documents_folder):
#             total_bytes = 0
#             sampled_files = []
#
#             # 遍历documents文件夹下的.json.gz文件
#             files = os.listdir(documents_folder)
#             json_gz_files = [file for file in files if file.endswith(".json.gz")]
#             random.shuffle(json_gz_files)
#             for file in files:
#                 file_path = os.path.join(documents_folder, file)
#                 # 获取文件大小
#                 file_size = os.path.getsize(file_path)
#                 total_bytes += file_size
#             total_sizes.append(total_bytes)
# total_sizes = [size * 1024 * 1024 * 1024 for size in total_sizes]

# 定义比例列表和文件夹名称列表
# 总量: 11+24+7.3+267+17+7.8+3.2+13+99+159+830+24+190+28+29
ratios = []

# 将GB数转换为字节数
GB_to_bytes = 1024 * 1024 * 1024
sample_sizes_bytes = [size * GB_to_bytes for size in sample_sizes]

# 遍历目录X下的文件夹
for folder_name in folders:
    folder_path = os.path.join(directory_X, folder_name)
    if os.path.isdir(folder_path):
        documents_folder = os.path.join(folder_path, "documents")
        if os.path.exists(documents_folder):
            sample_size = sample_sizes_bytes.pop(0)
            total_bytes = 0
            sampled_files = []

            # 遍历documents文件夹下的.json.gz文件
            files = os.listdir(documents_folder)
            json_gz_files = [file for file in files if file.endswith(".json.gz")]
            random.shuffle(json_gz_files)
            for file in json_gz_files:
                file_path = os.path.join(documents_folder, file)
                # 获取文件大小
                file_size = os.path.getsize(file_path)
                # 如果当前文件总大小未超过采样数，加入采样列表
                if total_bytes + file_size <= sample_size:
                    sampled_files.append(file_path)
                    total_bytes += file_size
                # 否则停止采样
                else:
                    break

            # 复制采样文件到目录Y下
            for file_path in sampled_files:
                file_name = os.path.basename(file_path)
                target_path = os.path.join(directory_Y, file_name)
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                shutil.copyfile(file_path, target_path)
