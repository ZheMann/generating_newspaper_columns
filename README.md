# Generating Dutch Newspaper Columns
This repo consists of three language models based on [GPT-2](https://github.com/openai/gpt-2)'s Small/Medium architecture, fine-tuned in different ways. These models can be used to generate samples, but they are also available for futher research/fine-tuning. The following language models are provided:
* Model 1. GPT-2 Medium (345M) pre-trained. Fine-tuned on a small dataset (2MB) for 30k training steps ~ 25 hours
* Model 2. GPT-2 Medium (345M) pre-trained. Fine-tuned on a large dataset (2.9GB) for 100k training steps ~ 3.5 days
* Model 3. GPT-2 Small (117M) from scratch. Fine-tuned on a large dataset (2.9GB) for 300k training steps ~ 4.2 days

## Requirements
* Colaboratory

### Colaboratory 
Log into your Google Account and go to Google Drive. Click on the New button on the left and then on 'More'. If:
a) 'Colaboratory' appears in the list, you do not have to do anything
b) 'Colaboratory' does not appear in the list, click on Connect more apps, search for Colaboratory and install it

## Training GPT-2 345M Pre-trained models
It is necessary to execute nexts steps if you want to train either Model 1 or Model 2:
1. Access the [models](https://drive.google.com/open?id=1j40vMmzc8sJnrDlLYELd_DvmyS9ktyUk) and add them to your Drive by right-clicking on the 'checkpoint' directory and selecting 'Add to my Drive'
2. Access the [encoded datasets](https://drive.google.com/open?id=1hn3c25BRF_VnBFrVoGQ4ubHsvE1IPWWK) and add them to your Drive by right-clicking on the 'encoded_data' directory and selecting 'Add to my Drive'

**Important Note:** Normally, you will only need to execute the steps above once. Unless you remove the models and datasets from your Drive.

### Model 1
To generate samples or to fine-tune Model 1:
1. Open the [Colaboratory Notebook](https://drive.google.com/open?id=1MY52FsRrsaeNColEQcWhdQZXCTrxY3Ie) in Colaboratory.
2. Make a copy of this Notebook (File -> Save a copy in Drive). This will open a copy in a new tab.
3. Reset all runtimes to prevent unwanted behaviour (Runtie -> Reset all runtimes..)
4. Perform Step 1 and its sub-steps
5. Perform Step 2 and its sub-steps to let the model generate samples
6. Perform Step 3 and its sub-steps to fine-tune the model on the encoded datasets

### Model 2
To generate samples or to fine-tune Model 2:
1. Open the [Colaboratory Notebook](https://drive.google.com/open?id=1muynamuFB-RS7FsHu0iNMLDVQ8g2fuAr) in Colaboratory.
2. Make a copy of this Notebook (File -> Save a copy in Drive). This will open a copy in a new tab.
3. Reset all runtimes to prevent unwanted behaviour (Runtie -> Reset all runtimes..)
4. Perform Step 1 and its sub-steps
5. Perform Step 2 and its sub-steps to let the model generate samples
6. Perform Step 3 and its sub-steps to fine-tune the model on the encoded datasets

## Training GPT-2 117M From scratch models
1. Access the [model](https://drive.google.com/open?id=1mHfMEn5MLVVOVIo2E5NDxS4GQClgUY0o) and add them to your Drive by right-clicking on the 'checkpoint' directory and selecting 'Add to my Drive'. This directory also contains the encoded datasets.
2. Access the [raw datasets](https://drive.google.com/open?id=17GnJC7I_l_XkQKbRtYFXvtnnpRvsmGxF) and add them to your Drive by right-clicking on the 'encoded_data' directory and selecting 'Add to my Drive'. These raw datasets are used during the training process of the SentencePiece model.

**Important Note:** Normally, you will only need to execute the steps above once. Unless you remove the models and datasets from your Drive.

### Model 3
To generate samples or to fine-tune Model 3:
1. Open the [Colaboratory Notebook](https://drive.google.com/open?id=1zyulaQ2yZ_eh97UngrgEW9AcXby9fD_P) in Colaboratory.
2. Make a copy of this Notebook (File -> Save a copy in Drive). This will open a copy in a new tab.
3. Reset all runtimes to prevent unwanted behaviour (Runtime -> Reset all runtimes..)
4. Perform Step 1 and its sub-steps
5. Perform Step 2 and its sub-steps to let the model generate samples
6. Perform Step 3 and its sub-steps to fine-tune the model on the encoded datasets
7. Perform Step 4 and its sub-steps to see how to the SentencePiece model is trained as well as how the datasets are encoded

## Datasets used
We used the following datasets to fine-tune the language models, which can be accessed [here](https://drive.google.com/open?id=17GnJC7I_l_XkQKbRtYFXvtnnpRvsmGxF):
1. Dutch newspaper columns (2MB) 
2. Dutch Wikipedia-pages (2.9GB)
3. Dutch e-books (24MB)

### Dutch newspaper columns (2MB)
These newspaper columns were provided by a collaborating journalist during this research. The body of each columns is extracted and concatenated into a single text-file. Due to inconsistency between columns, most pre-processing is done manually.

### Dutch Wikipedia-pages (2.9GB)
We built our own [wiki-scraper](https://github.com/ZheMann/wiki-scraper) to extract information from Wikipedia. The wiki-scraper ran for several days untill 2.4M out of 2.6M pages were downloaded. The text of all pages is concatenated into a single text-file.

### Dutch e-books (24MB)
Project Gutenborg provides free, mostly older, e-books in several languages from which the copyright has expired. For this, we built a [Colaboratory Notebook](https://drive.google.com/open?id=1WCkbCMCay9a4NaUv7boAJjfCQ10JKUjv) to download all books for the Dutch language, to extract the right files and to concatenate the books into a single text-file. In addition, we had to manually remove English disclaimers from each book.

## About this repository
This repository is built to support my Research Internship as a first year master student in Computing Science (April 2019 - July 2019).  During this research an experiment is performed, consisting of generating texts by three differently trained language models, as discussed in previous sections.
