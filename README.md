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
We used the following datasources to fine-tune the language models:
1. Dutch Newspaper columns (2MB)
2. Dutch Wikipedia-pages (2.9GB) by the implementation of a custom [wiki-scraper](https://github.com/ZheMann/wiki-scraper)
3. Dutch E-books (24MB) by 

## Training GPT-2 345M Pre-trained models
It is necessary to execute nexts steps if you want to train either Model 1 or Model 2:
1. Access the pre-trained models through [this](https://drive.google.com/open?id=1j40vMmzc8sJnrDlLYELd_DvmyS9ktyUk) link
2. Right-click on the 'checkpoint' directory and select 'Add to my Drive'
3. Access the encoded [datasets](https://drive.google.com/open?id=1hn3c25BRF_VnBFrVoGQ4ubHsvE1IPWWK) datasets
4. Right-click on the 'encoded_data' directory and select 'Add to my Drive'

**Important Note:** You only need to execute the steps above once, since you have to save the directories 'checkpoint' and 'encoded_data' to your Google Drive.

### Model 1
1. Access the [Colaboratory Notebook](https://drive.google.com/open?id=1MY52FsRrsaeNColEQcWhdQZXCTrxY3Ie) to fine-tune Model 1.


### Model 2
1. Access the [Colaboratory Notebook]() to fine-tune Model 2.


3. Open [this](https://drive.google.com/open?id=1iwsGZJqctjoVK-i5FwGhijYFPBCHxRx2) file in Google Colaboratory
4. Follow the steps 

## About this repository
This repository is built to perform the experiments during my Research Internship as a first year master student in Computing Science (April 2019 - July 2019).  The experiment consisted of generating texts by three differently trained language models, as mentioned in Language Models.
