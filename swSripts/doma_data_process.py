import os
import glob
import uuid
import pandas as pd
import argparse

def convert_to_dolma_format(parquet_dir,output_dir, source="story", prefix="tinyStories_"):
    """
    将指定目录下的所有 train-*.parquet 文件转换为符合 Dolma 格式的 parquet 文件。
    
    参数：
        parquet_dir (str): parquet 文件所在的目录路径
        source (str): 自定义的 source 字段值，默认是 "unknown"
        prefix (str): 输出文件名前缀，默认是 "dolma_"

    i_dir:/mnt/zzb/peixunban/zzb6/data/swZheng/dataSet/raw/TinyStories2/TinyStories/data/
    o_dir:/mnt/zzb/peixunban/zzb6/data/swZheng/dataSet/selected/tinyStoriesData
    """
    pattern = os.path.join(parquet_dir, "train-*.parquet")
    files = glob.glob(pattern)

    if not files:
        print(f"未在目录 {parquet_dir} 中找到符合 train-*.parquet 的文件。")
        return

    for path in files:
        print(f"处理文件: {path}")
        df = pd.read_parquet(path)

        if "text" not in df.columns:
            print(f"跳过文件（缺少 text 字段）: {path}")
            continue

        df["id"] = [str(uuid.uuid4()) for _ in range(len(df))]
        df["source"] = source
        df = df[["id", "text", "source"]]

        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, prefix + os.path.basename(path))
        df.to_parquet(output_path, index=False)
        print(f"已保存为: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Convert Parquet files to Dolma format")
    parser.add_argument("--i_dir", type=str, required=True, help="Parquet 文件所在目录")
    parser.add_argument("--o_dir", type=str, required=True, help="Parquet 输出目录")
    parser.add_argument("--source", type=str, default="story", help="source 字段值")
    parser.add_argument("--prefix", type=str, default="tinyStories_", help="输出文件名前缀")

    args = parser.parse_args()

    convert_to_dolma_format(parquet_dir=args.i_dir, output_dir=args.o_dir, source=args.source, prefix=args.prefix)

if __name__ == "__main__":
    main()