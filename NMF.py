# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 15:03:48 2017

@author: JohannesM
"""
from pandas.tools.plotting import scatter_matrix
import numpy as np  # a conventional alias
import pandas as pd
import sklearn.feature_extraction.text as text
from sklearn import decomposition
from string import digits

num_topics = 11
num_top_words = 15

#get stop words
stop_file = open("stop_words.txt","r")
stop_words = stop_file.read().decode('latin-1').split('\n')

print stop_words


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
    
    clf = decomposition.NMF(n_components=num_topics, random_state=1)
    matrix=clf.fit_transform(dtm)
    
    print_top_words(clf, vectorizer)
    
    return matrix

    
def Dirichlet(documents, vectorizer):
    dtm = vectorizer.fit_transform(documents).toarray()


    lda = decomposition.LatentDirichletAllocation(n_topics=num_topics, max_iter=50,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0,
                                verbose=1,
                                evaluate_every=1,                                
                                doc_topic_prior=0.2,
                                topic_word_prior = 0.6)
    lda.fit(dtm)

    print_top_words(lda,vectorizer)
    
    return lda

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
Tfidf = text.TfidfVectorizer(max_df=0.9, min_df=0.2, stop_words = stop_words)              
CountVector =  text.CountVectorizer(max_df=0.9 ,min_df=0.2,  stop_words = stop_words)  


for date in dates:
    total_text = ""
    for cellText in p08_df[p08_df['Datum']==date]['Text'].values:
        total_text += str(cellText) + '\n'
    #remove all numbers 
    total_text = total_text.translate(None, digits)    
    documents.append(total_text)


#dropping english topics
documents.pop(9)
documents.pop(8)

 

print("\nCount weights Non-Negative Matrix factorization")
NMF_clf = NMF(documents, CountVector)
print("\nTFIDF word weights Non-Negative Matrix factorization")
NMF_tfidf_clf = NMF(documents, Tfidf)
print("\nCount weights Latent Dirichlet Allocation")
Dirichlet(documents,CountVector)


#plot scatter plots for 2 topics with NMF
#df_columns=['topic1','topic2','topic3','topic4','topic5']



#NMF_df=pd.DataFrame(data=NMF_tfidf_clf,    # values
              #columns=df_columns)

#scatter_matrix(NMF_df,alpha=0.8, figsize=(6, 6))
#len(vocab)