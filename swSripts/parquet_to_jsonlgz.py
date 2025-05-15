import pandas as pd
import json
import gzip
import glob
import os
from multiprocessing import Pool

# 定义输入目录和输出目录
# input_directory = '/mnt/zzb/peixunban/zzb6/data/swZheng/dataSet/raw/TinyStories2/TinyStories/data'
# output_directory = '/mnt/zzb/peixunban/zzb6/data/swZheng/dataSet/preTrainJsonL/tinyStories/documents/'
input_directory = '/mnt/zzb/peixunban/zzb6/home/swZheng/sftData/tulu/tulu-3-sft-mixture/data'
output_directory = '/mnt/zzb/peixunban/zzb6/home/swZheng/sftData/tulu/tulu-3-sft-mixture/data_json'

# 如果输出目录不存在，创建它
os.makedirs(output_directory, exist_ok=True)

# 获取目录下所有后缀为.parquet的文件
parquet_files = glob.glob(os.path.join(input_directory, '*.parquet'))

def process_file(parquet_file):
    try:
        print('Begin parsing file:', parquet_file)

        # 读取.parquet文件
        data = pd.read_parquet(parquet_file)

        # 添加source列
        data['source'] = 'tinyStories'

        # 判断是否有id字段，如果没有则生成id
        if 'id' not in data.columns:
            data['id'] = [str(i) for i in range(len(data))]  # 生成唯一的id

        # 转换为字典列表
        dict_list = data.to_dict(orient='records')

        # 构造输出文件名（只取文件名，不带路径）
        base_name = os.path.splitext(os.path.basename(parquet_file))[0]
        jsonl_file_path = os.path.join(output_directory, base_name + '.jsonl')

        # 保存为jsonl文件
        with open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:
            for item in dict_list:
                jsonl_file.write(json.dumps(item) + '\n')

        # 压缩成jsonl.gz文件
        with open(jsonl_file_path, 'rb') as f_in:
            with gzip.open(jsonl_file_path + '.gz', 'wb') as f_out:
                f_out.writelines(f_in)

        # 删除原始jsonl文件，只保留压缩后的jsonl.gz
        os.remove(jsonl_file_path)

        print('File {} finished'.format(parquet_file))

    except Exception as e:
        print(f'Error processing {parquet_file}: {e}')

if __name__ == '__main__':
    # 创建进程池，开20个进程
    with Pool(processes=20) as pool:
        pool.map(process_file, parquet_files)
