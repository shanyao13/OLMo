from hf_olmo import * # registers the Auto* classes

from transformers import AutoModelForCausalLM, AutoTokenizer

# 首先要将olmo的模型转化为transformer format：执行模型转化
# python scripts/convert_olmo_to_hf_new.py --input_dir "/mnt/zzb/peixunban/zzb6/home/swZheng/OLMo/tmp/output-1B/step114000-unsharded" --tokenizer_json_path "olmo_data/tokenizers/allenai_eleuther-ai-gpt-neox-20b-pii-special.json" --output_dir "/mnt/zzb/peixunban/zzb6/home/swZheng/OLMo/tmp/output-1B-infer_model"

olmo = AutoModelForCausalLM.from_pretrained("/mnt/zzb/peixunban/zzb6/home/swZheng/OLMo/tmp/output-1B-infer_model-step177/")
tokenizer = AutoTokenizer.from_pretrained("/mnt/zzb/peixunban/zzb6/home/swZheng/OLMo/tmp/output-1B-infer_model-step177/")

# message = ["Language modeling is "]
message = ["数学是科学的"]
print(f"Input: {message}")
inputs = tokenizer(message, return_tensors='pt', return_token_type_ids=False)
response = olmo.generate(**inputs, max_new_tokens=100, do_sample=True, top_k=50, top_p=0.95)
# print(f"response: {response}")
result = tokenizer.batch_decode(response, skip_special_tokens=True)[0]
print(f"Output: {result}")

# print(tokenizer.decode(tokenizer.encode("Hello world!")))