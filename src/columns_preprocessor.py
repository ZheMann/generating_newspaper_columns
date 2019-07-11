import nltk

''' 
    Use this method when you already have the files preprocessed.
    This means: only the body of each column is present in the file, 
    separated from each other by a white line
    
    This method replaces the white lines with an end and start tag,
    as this (should) improve(s) the quality of GPT-2 model.
    
    Store input files in directory 'input'
    Processed files can be found in directory 'output' 
'''
def transform_preprocessed_file(filename, append_to_file):
    o_path = "./data/processed_files/input/{0}.txt".format(filename)

    if append_to_file:
        p_path = "./data/processed_files/output/combined.txt"
    else:
        p_path = "./data/processed_files/output/{0}_processed.txt".format(filename)

    with open(o_path, "r", encoding="utf-8") as original_file:
        with open(p_path, "a", encoding="utf-8") as processed_file:
            processed_file.write("<|startoftext|>\n")

            for line in original_file:
                if not line.strip():
                    line = "<|endoftext|>\n<|startoftext|>\n"

                processed_file.write(line)

            processed_file.write("\n<|endoftext|>\n")


'''
    Use this method for the original files provided by the journalist. 
    However, you are required to transform the .docx-files to .txt-files first as this method expects plain text-files.
    
    This method checks each line whether it has 0 words (white line) or less or equal tan four words.
    If so, the line is most likely placed within the header of a column. These lines are removed as we are only 
    interested in the body of a column.
    However, this is a rough assumption and therefor we also take the previous line into account. 
    If current line has four or less words, but the previous line has seven or more words, the sentence most likely
    still belongs to the body of a column.
    
    To add the start and end tags, we assume the email-adress of the journalist to indicate the end of a column. We 
    therefore replace each email-adres within the file with the start and end tag. 
    
    Although this methods works OK, it is far from perfect where as some errors/bugs still might occur. 
    This is mainly due to the inconsistent construction of each file. 
    For example, columns of 2013 are not provided withthe journalist's email-address 
    whereby it is not possible to replace it with start and end tags. 
'''
def transform_original_file(filename):
    o_path = "./data/original_files/input/{0}.txt".format(filename)
    p_path = "./data/original_files/output/{0}_processed.txt".format(filename)

    with open(o_path, "r", encoding="utf-8") as original_file:
        with open(p_path, "a", encoding="utf-8") as processed_file:
            processed_file.write("<|startoftext|>")
            prev_word_count = 0
            for line in original_file:
                write_line = True

                # Use nltk tokenizer for nb. of words in current line
                cur_word_count = len(nltk.word_tokenize(line))

                # If a sentence has four or less words, it can be found most likely in the header of a column,
                # or it is a line that consists of solely whitespaces. We want to ignore these lines.
                # However, it is possible that such a short sentence appears in the middle or end of a column.
                # Therefore we also check the length of previous sentence. If the previous sentence has seven
                # or more words, we consider the short sentence to belong to the column.
                if cur_word_count == 0:
                    write_line = False
                elif cur_word_count <= 4:
                    if prev_word_count < 7:
                        write_line = False

                if write_line:
                    processed_file.write(line)

                # Set nb. of words
                prev_word_count = cur_word_count

    # Majority of columns end with 'asing.walthaus@lc.nl' or '> asing.walthaus@lc.nl'.
    # As this is not necessary for our text generator, we can use this to indicate the end (start) of the current
    # (next) column.
    r = open(p_path, "r", encoding="utf-8").read()
    r = r.replace("> asing.walthaus@lc.nl", "<|endoftext|>\n<|startoftext|>")
    r = r.replace("asing.walthaus@lc.nl", "<|endoftext|>\n<|startoftext|>")
    w = open(p_path, "w", encoding="utf-8")
    w.write(r)


def create_csv_wo_whitelines():
    path = './data/combined.txt'
    path_new = './data/combined_wo_whitelines.csv'

    start_text = "<|startoftext|>"
    end_text = "<|endoftext|>"
    with open(path, 'r', encoding='utf8', errors='ignore') as fp:
        with open(path_new, 'a', encoding='utf8', errors='ignore') as fp2:
            fp2.write("header\n")
            for line in fp:
                if ''.join(line).startswith(start_text):
                    continue
                if ''.join(line).startswith(end_text):
                    continue
                if not ''.join(line).strip():
                    continue

                fp2.write(line)


def append_to_file(filename):
    o_path = "./data/processed_files/input/{0}.txt".format(filename)
    p_path = "./data/combined.txt"

    with open(o_path, "r", encoding="utf-8") as original_file:
        with open(p_path, "a", encoding="utf-8") as processed_file:
            for line in original_file:
                processed_file.write(line)


''' Columns written in 2013 are the only ones without 'asing.walthaus@lc.nl' at the end of the column. Therefore,
this file needs to be manually preprocessed in order to obtain optimal results. All other files can be processed
via this file.'''
if __name__ == '__main__':
    # Make sure files are a) saved as UTF-8(!) and b) are stored in:
    # a) ./data/original_files/input/ when using transform_original_file (see comments above method for add. info)
    # b) ./data/processed_files/input/ when using transform_preprocessed_file (see comments above method for add. info)
    file_names = ["columns2011-2010",
                  "columns2012",
                  "columns2014",
                  "columns2015",
                  "columns2016",
                  "columns2017",
                  "columns2018",
                  "columns2019"]

    file_2013 = "columns2013"

    for file in file_names:
        append_to_file(file)

    append_to_file(file_2013)
    # for file in file_names:
    #     transform_preprocessed_file(file, True)
    #
    # transform_preprocessed_file(file_2013, True)
