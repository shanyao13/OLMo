 dolma tag \
    --documents "selectedFromDolma/documents/*" \
    --experiment exp \
    --taggers random_number_v1 \
              cld2_en_paragraph_with_doc_score_v2 \
              ft_lang_id_en_paragraph_with_doc_score_v2 \
              char_length_with_paragraphs_v1 \
              whitespace_tokenizer_with_paragraphs_v1 \
    --processes 20 > dolma_tag_log.txt 2>&1 &

dolma tag \
  --documents "selectedFromDolma/documents/*" \
  --destination "selectedFromDolma/processed" \
  --taggers cld2_en_paragraph_with_doc_score_v2 \
           ft_lang_id_en_paragraph_with_doc_score_v2 \
           char_length_with_paragraphs_v1 \
           whitespace_tokenizer_with_paragraphs_v1 \
  --experiment exp3 \
  --processes 20 \
  --no-ignore_existing > dolma_tag_log3.txt 2>&1 &

  dolma tag \
   --documents "pretrain/samples/documents/*" \
   --experiment exp \
   --taggers random_number_v1 \
             ft_lang_id_en_paragraph_with_doc_score_v2 \
             char_length_with_paragraphs_v1 \
            whitespace_tokenizer_with_paragraphs_v1 \
   --processes 20 > dolma_tag_log3.txt 2>&1 &


   dolma tag \
   --documents "tinyStories/documents/*" \
   --destination "./tinyStories/processed" \
   --experiment exp \
   --taggers random_number_v1 \
            ft_lang_id_en_paragraph_with_doc_score_v2 \
            char_length_with_paragraphs_v1 \
            whitespace_tokenizer_with_paragraphs_v1 \
   --processes 20  > tagTinystoryLog.txt 2>&1 &
