import gzip
import json

file_path = "/mnt/zzb/peixunban/zzb6/data/swZheng/dataSet/selected/selectedFromDolma/documents/c4-0166.json.gz"

with gzip.open(file_path, "rt", encoding="utf-8", errors="ignore") as f:
    for idx, line in enumerate(f, 1):  # 按行遍历，idx 是文档编号
        try:
            doc = json.loads(line)
            paragraphs = doc.get("paragraphs", [])
            for p_idx, paragraph in enumerate(paragraphs):
                text = paragraph.get("text", "")
                if "\x00" in text:
                    print(f"[Line {idx}] Paragraph {p_idx} contains NULL char:")
                    null_positions = [i for i, ch in enumerate(text) if ch == '\x00']
                    print(f"  -> Positions: {null_positions}")
                    print(f"  -> Snippet: {repr(text[max(0, null_positions[0]-20):null_positions[0]+20])}")
        except Exception as e:
            print(f"[Line {idx}] Failed to parse JSON: {e}")


# 查看前5行
# zcat /mnt/zzb/peixunban/zzb6/data/swZheng/dataSet/selected/selectedFromDolma/documents/c4-0166.json.gz | head -n 5