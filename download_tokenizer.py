from transformers import AutoTokenizer

# This downloads the t5-base tokenizer files to a local directory
tokenizer = AutoTokenizer.from_pretrained('t5-base')

# This saves the files to a new directory named 't5-base_tokenizer'
tokenizer.save_pretrained('amrlib/data/t5-base_tokenizer')