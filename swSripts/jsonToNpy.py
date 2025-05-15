import dolma
import numpy as np
from transformers import AutoTokenizer
import json

# Step 1: 使用 dolma 读取 jsonl 数据
data = dolma.io.read_jsonl('/mnt/zzb/peixunban/zzb6/data/swZheng/localData/global-shard_01_of_10/local-shard_1_of_10/shard_00000278_processed.jsonl')

# Step 2: 使用 Hugging Face 分词器进行分词（假设使用 BERT tokenizer）
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

# Step 3: 设置 chunk_size，确保每个样本的 token 数量适配 OLMo 模型的输入需求
chunk_size = 512  # 可以根据 OLMo 模型的实际需求调整

# Step 4: 将每条数据进行分词，并转换为 token ids
processed_data = []
for item in data:
    # 获取文本字段
    text = item['text']  # 假设 jsonl 中的每一行包含 'text' 字段
    
    # 分词：处理 padding 和 truncation，以确保每个样本的 token 长度为 chunk_size
    tokenized = tokenizer(text, padding='max_length', truncation=True, max_length=chunk_size, return_tensors="np")
    
    # 获取 token_ids 并添加到 processed_data 中
    processed_data.append(tokenized['input_ids'])

# Step 5: 将处理后的数据保存为 npy 格式
npy_data = np.array(processed_data)
np.save('./processed_data.npy', npy_data)

print("数据已成功转换并保存为 npy 格式！")

