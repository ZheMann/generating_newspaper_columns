# Generating Dutch Newspaper Columns
This repository is used to fine-tune [GPT-2](https://github.com/openai/gpt-2) in two different ways, namely:
1. Fine-tuning GPT-2 pre-trained 
2. Fine-tuning GPT-2 from scratch, i.e. without any prior knowledge/data.

# Language Models
This repo consists of three language models based on GPT-2's Small/Medium architecture, fine-tuned in different ways:
1. GPT-2 Medium (345M) pre-trained. Fine-tuned on a small dataset (2MB)
2. GPT-2 Medium (345M) pre-trained. Fine-tuned on a large dataset (2.9GB)
3. GPT-2 Small (117M) from scratch. Fine-tuned on a large dataset (2.9GB)

### GPT-2 Medium (345M) pre-trained. Fine-tuned on a small dataset (2MB)

### GPT-2 Medium (345M) pre-trained. Fine-tuned on a large dataset (2.9GB)

### GPT-2 Small (117M) from scratch. Fine-tuned on a large dataset (2.9GB)

# Datasets
The following datasets are used to fWe used the following datasources to fine-tune the language models:
1. Dutch Newspaper columns (2MB)
2. Dutch Wikipedia-pages (2.9GB)
3. Dutch E-books (24MB)

# About this repository
This repository is built to perform the experiments during my Research Internship as a first year master student in Computing Science (April 2019 - July 2019).  The experiment consisted of generating texts by three differently trained language models, as mentioned in Language Models.
