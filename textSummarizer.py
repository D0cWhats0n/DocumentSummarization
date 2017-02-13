# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.sum_basic import SumBasicSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import os

#set language and sentence count
LANGUAGE = "english"
SENTENCES_COUNT = 6
dir = os.path.dirname(__file__)

concat_string = ""

def readFileAsString(path):
    with open(path, 'r') as myfile:
        data=myfile.read().replace('\n', '')
    return data



#read files from directory
for file in os.listdir(path):
    if file.endswith(".txt"):
        
        concat_string = readFileAsString(dir +"/textFiles/" + file) 
        
parser = PlaintextParser.from_string(concat_string, Tokenizer(LANGUAGE))
stemmer = Stemmer(LANGUAGE)

summarizer = Summarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)

for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence)




