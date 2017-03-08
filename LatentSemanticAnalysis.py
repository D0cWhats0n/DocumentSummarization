# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 15:03:48 2017

@author: JohannesM
"""

import numpy as np  # a conventional alias
import pandas as pd
import sklearn.feature_extraction.text as text
from sklearn import decomposition

num_topics = 5
num_top_words = 10


def concatString(stringArr):
    concatString = ""
    for string in stringArr:
        concatString += " " + string.encode('utf-8')
    return concatString

p08_df = pd.read_csv('protocol_edited.txt', delimiter=';')
p08_df['Text'].str.decode('utf-8')
concat_string = p08_df['Text'].values                     

#get possible date values to regain documents                      
dates = p08_df.drop_duplicates('Datum')['Datum']          
    
#Concatinate strings of same document and store them in documents
documents = []    
              
for date in dates:
    total_text = ""
    for cellText in p08_df[p08_df['Datum']==date]['Text'].values:
        total_text += str(cellText) + '\n'
    documents.append(total_text)


vectorizer = text.CountVectorizer(max_df=0.2 ,min_df=0)
dtm = vectorizer.fit_transform(documents).toarray()
vectorizer.fit_transform(documents)

vocab = np.array(vectorizer.get_feature_names())

print len(vocab)

print dtm.shape


clf = decomposition.NMF(n_components=num_topics, random_state=1)

doctopic = clf.fit_transform(dtm)

topic_words = []
for topic in clf.components_:
   word_idx = np.argsort(topic)[::-1][0:num_top_words]
   topic_words.append([vocab[i] for i in word_idx])


for t in range(len(topic_words)):
   print "Topic {}: {}".format(t, ' ' + concatString(topic_words[t][:num_top_words]))

#len(vocab)