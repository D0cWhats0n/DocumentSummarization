# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from IPython.display import display
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.sum_basic import SumBasicSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import numpy as np
import pandas as pd
import os

#set language and sentence count
LANGUAGE = "german"
SENTENCES_COUNT = 3
filePath = os.path.dirname(__file__)+ "/textFiles/"

concat_string = ""

total_text= " "
#read files from directory
#test_df = pd.DataFrame()
#for file in os.listdir(filePath):
#    test_df = readTableAsDataFrame(filePath + file)
#    concat_string += readFileAsString(filePath + file) 

p08_df = pd.read_csv('protocol_edited.txt', delimiter=';')
        
p08_df['Text'].str.decode('utf-8')

concat_string = p08_df['Text'].values


parser = PlaintextParser.from_string(total_text, Tokenizer(LANGUAGE))
stemmer = Stemmer(LANGUAGE)

summarizer = Summarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)

#for sentence in summarizer(parser.document, SENTENCES_COUNT):
#    print(sentence)




