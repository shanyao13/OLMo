from hf_olmo import * # registers the Auto* classes

from transformers import AutoModelForCausalLM, AutoTokenizer

olmo = AutoModelForCausalLM.from_pretrained("/root/swZheng/dev/OLMo/tmp/checkpoints/OLMo-1B/step138-unsharded/infer_model/")
tokenizer = AutoTokenizer.from_pretrained("/root/swZheng/dev/OLMo/tmp/checkpoints/OLMo-1B/step138-unsharded/infer_model/")

message = ["Language modeling is "]
print(f"Input: {message}")
inputs = tokenizer(message, return_tensors='pt', return_token_type_ids=False)
response = olmo.generate(**inputs, max_new_tokens=100, do_sample=True, top_k=50, top_p=0.95)
print(f"response: {response}")
result = tokenizer.batch_decode(response, skip_special_tokens=True)[0]
print(f"Output: {result}")

print(tokenizer.decode(tokenizer.encode("Hello world!")))