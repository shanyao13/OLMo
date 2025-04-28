import pandas as pd
import glob
import os
import json
import gzip

def parquet_to_json_gz(parquet_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    files = glob.glob(os.path.join(parquet_dir, "*.parquet"))

    for path in files:
        df = pd.read_parquet(path)
        
        # 检查是否包含必要字段
        if not {"id", "text", "source"}.issubset(df.columns):
            print(f"跳过 {path}，缺少必须字段")
            continue

        base = os.path.basename(path).replace(".parquet", ".json.gz")
        out_path = os.path.join(output_dir, base)

        print(f"转换中: {path} ➜ {out_path}")

        with gzip.open(out_path, "wt", encoding="utf-8") as zipfile:
            for record in df.to_dict(orient="records"):
                zipfile.write(json.dumps(record, ensure_ascii=False) + "\n")

        print(f"已完成: {out_path}")

# 示例调用
if __name__ == "__main__":
    parquet_to_json_gz(
        parquet_dir="/mnt/zzb/peixunban/zzb6/data/swZheng/dataSet/selected/tinyStoriesData",
        output_dir="/mnt/zzb/peixunban/zzb6/data/swZheng/dataSet/selected/tinyStoriesData_json/documents"
    )
