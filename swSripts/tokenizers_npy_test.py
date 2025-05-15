from transformers import AutoTokenizer
import numpy as np

# tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-neox-20b')
tokenizer = AutoTokenizer.from_pretrained('allenai/eleuther-ai-gpt-neox-20b-pii-special'
    )


with open('/mnt/zzb/peixunban/zzb6/data/zjf_zsw/tokenizer1/part-19-00000.npy', 'rb') as f:
    data = np.fromfile(f, dtype=np.uint16)
print(data.shape)
print(tokenizer.decode(data[:1000]))

