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
num_features = 1000

def print_top_words(clf, vectorizer):
    topic_words = []
    vocab = np.array(vectorizer.get_feature_names())
    for topic in clf.components_:
        word_idx = np.argsort(topic)[::-1][0:num_top_words]
        topic_words.append([vocab[i] for i in word_idx])

    for t in range(len(topic_words)):
        print "Topic {}: {}".format(t, ' ' + concatString(topic_words[t][:num_top_words]))


def NMF(documents, vectorizer):
    dtm = vectorizer.fit_transform(documents).toarray()
    vectorizer.fit_transform(documents)
    
    clf = decomposition.NMF(n_components=num_topics, random_state=1)
    clf.fit_transform(dtm)
    
    print_top_words(clf, vectorizer)

    
def Dirichlet(documents, vectorizer):
    dtm = vectorizer.fit_transform(documents).toarray()
    vectorizer.fit_transform(documents)
    
    lda = decomposition.LatentDirichletAllocation(n_topics=num_topics, max_iter=5,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)
    lda.fit(dtm)
    
    print_top_words(lda,vectorizer)

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
#vectorizer = text.CountVectorizer(max_df=0.2 ,min_df=0)   
Tfidf = text.TfidfVectorizer(max_df=0.2, min_df=0)              
CountVector =  text.CountVectorizer(max_df=0.2 ,min_df=0)  

for date in dates:
    total_text = ""
    for cellText in p08_df[p08_df['Datum']==date]['Text'].values:
        total_text += str(cellText) + '\n'
    documents.append(total_text)


print("\nCount weights Non-Negative Matrix factorization")
NMF(documents, CountVector)
print("\nTFIDF word weights Non-Negative Matrix factorization")
NMF(documents, Tfidf)
print("\nCount weights Latent Dirichlet Allocation")
Dirichlet(documents,CountVector)
print("\nTFIDF Latent Dirichlet Allocation")
Dirichlet(documents,Tfidf)




#len(vocab)