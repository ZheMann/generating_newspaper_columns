# Generating Dutch Newspaper Columns
This repository is used to fine-tune two different types of [GPT-2](https://github.com/openai/gpt-2), namely:
1. Fine-tuning pre-trained models of GPT-2
2. Fine-tuning GPT-2 models from scratch, i.e. without any prior training.

## Requirements
* Colaboratory

### Colaboratory 
Log into your Google Account and go to Google Drive. Click on the New button on the left and then on 'More'. If:
a) 'Colaboratory' appears in the list, you do not have to do anything
b) 'Colaboratory' does not appear in the list, click on Connect more apps, search for Colaboratory and install it

## Language Models
This repo consists of three language models based on GPT-2's Small/Medium architecture, fine-tuned in different ways. These models can be used to generate samples, but they are also available for futher research/fine-tuning. The following language models are trained:
1. GPT-2 Medium (345M) pre-trained. Fine-tuned on a small dataset (2MB) for 30k training steps ~ 25 hours
2. GPT-2 Medium (345M) pre-trained. Fine-tuned on a large dataset (2.9GB) for 100k training steps ~ 3.5 days
3. GPT-2 Small (117M) from scratch. Fine-tuned on a large dataset (2.9GB) for 300k training steps ~ 4.2 days

## Datasets
We used the following datasets to fine-tune the language models:
1. Dutch Newspaper columns (2MB) 
2. Dutch Wikipedia-pages (2.9GB) by the implementation of a custom [wiki-scraper](https://github.com/ZheMann/wiki-scraper)
3. Dutch E-books (24MB) by a [Colaboratory Notebook](https://drive.google.com/open?id=1WCkbCMCay9a4NaUv7boAJjfCQ10JKUjv)

## Training GPT-2 345M Pre-trained models
It is necessary to execute nexts steps if you want to train either Model 1 or Model 2:
1. [Access](https://drive.google.com/open?id=1j40vMmzc8sJnrDlLYELd_DvmyS9ktyUk) the models and add them to your Drive by right-clicking on the 'checkpoint' directory and selecting 'Add to my Drive'
2. [Access](https://drive.google.com/open?id=1hn3c25BRF_VnBFrVoGQ4ubHsvE1IPWWK) the encoded datasets and add them to your Drive by right-clicking on the 'encoded_data' directory and selecting 'Add to my Drive'

**Important Note:** Normally, you will only need to execute the steps above once. Unless you remove the models and datasets from your Drive.

### Model 1
1. Access the [Colaboratory Notebook](https://drive.google.com/open?id=1MY52FsRrsaeNColEQcWhdQZXCTrxY3Ie) to fine-tune Model 1.
2. Perform Step 1 and its sub-steps
3. Perform Step 2 and its sub-steps to let the model generate samples
4. Perform Step 3 and its sub-steps to fine-tune the model on the encoded datasets


### Model 2
1. Access the [Colaboratory Notebook]() to fine-tune Model 2.


## About this repository
This repository is built to support my Research Internship as a first year master student in Computing Science (April 2019 - July 2019).  During this research an experiment is performed, consisting of generating texts by three differently trained language models, as discussed in previous sections.
