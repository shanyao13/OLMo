import argparse
import pandas as pd

def read_parquet(input_path):
    # 读取本地 parquet 文件
    #df = pd.read_parquet("../raw/2_3/000001.parquet")
    df = pd.read_parquet(input_path)

    # 查看前几行
    print(df.head())

    # 查看列名
    print(df.columns)

    # 假设你想打印文本列（如果有）：
    #if 'text' in df.columns:
    #    for i, row in df.iterrows():
    #        print(row['text'][:200])  # 打印每条文本前200字符


def main():
    # input_path = "/mnt/zzb/peixunban/zzb6/data/swZheng/dataSet/selected/tinyStoriesData/tinyStories_train-00000-of-00004-2d5a1467fff1081b.parquet"
    # read_parquet(input_path)
    parser = argparse.ArgumentParser(description="Read Parquet files")
    parser.add_argument("--i_path", type=str, required=True, help="Parquet 文件所在路径")

    args = parser.parse_args()

    read_parquet(input_path=args.i_path)

if __name__ == "__main__":
    main()