# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import StringIO
from docx import Document
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.sum_basic import SumBasicSummarizer as Summarizer
from sumy.summarizers.lex_rank import LexRankSummarizer as LexSummarizer 
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import os

#set language and sentence count
LANGUAGE = "german"
SENTENCES_COUNT = 5
filePath = os.path.dirname(__file__)+ "/textFiles/"

concat_string = ""

def readFileAsString(path):
   with open(path, 'rb') as f:
    source_stream = StringIO(f.read())
    document = Document(source_stream)
    # with open(path, 'r') as myfile:
    #    data=myfile.read().replace('\n', '')
    return document



#read files from directory
for file in os.listdir(filePath):
    if file.endswith(".docx"):  
        concat_string += "\n" + readFileAsString(filePath + file) 
        
parser = PlaintextParser.from_string(concat_string, Tokenizer(LANGUAGE))
stemmer = Stemmer(LANGUAGE)

summarizer = Summarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)

for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence)




