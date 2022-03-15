import gzip
import random
from tkinter import S
from venv import create
import nltk
from turtle import pos
from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

def sample_lines(path, lines):
    line_list = []
    with gzip.open(path, 'rt') as file:
        for line in file:
            if '\x00' in line or '\n' == line:
                continue
            line_list.append(line)
    try:
        randomList = []
        randomIndex = random.sample(range(len(line_list)), lines)
        for num in randomIndex:
            randomList.append(line_list[num])
    except:
        print("Someting went wrong! Maybe out of index, but retruned list is shuffed.")
    finally:
        randomList = []
        randomIndex = random.sample(range(len(line_list)), len(line_list))
        for num in randomIndex:
            randomList.append(line_list[num])
    
    return randomList


def process_sentences(sentList):
    clean_list = []
    for sent in sentList:
        sent = word_tokenize(sent.lower())
        wordWithTag = nltk.pos_tag(sent)

        # Remove stop words and puncs
        stopWords = set(stopwords.words('english'))
        puncs = '''!()-[]{};:'"\,<>./?@#$%^&*_~—'''

        clean_word_tag = []
        for w, t in wordWithTag:
            if w not in stopWords and w not in puncs:
                clean_word_tag.append((w, t))
        clean_list.append(clean_word_tag)
        
    return clean_list

# The retuned samples only predict verb
def create_samples(cleanList, samples=50000):
    span = 5
    the_third_word_tag = [] # keep the 3rd word in this list
    five_list = []
    for l in cleanList:
        for i in range(0, len(l)):
            if len(l[i: i+span]) == 5:
                five_word_tag = l[i: i+span]  
                four_word_positon_tag = []
                
                # take last two letters and add position
                for i in range(len(five_word_tag)):
                    w, t = five_word_tag[i]

                    if i != 2 :
                        four_word_positon_tag.append(w[-2:] +"_" + str(i))
                
                allTags = ['VB', 'VBG', 'VBD', 'VBN', 'VBP', 'VBZ','NN', 'NNS', 'NNP', 'NNPS',
                                'JJ', 'JJR', 'JJS','RB', 'RBR', 'RBS']
                _, third_tag = five_word_tag[2]
                the_third_word_tag.append(third_tag)    # keep the third word tag
                
                # the_third_word_tag.append(four_word_positon_tag[2])
                if third_tag not in allTags:
                    continue
                else:
                    five_list.append((third_tag[:2], four_word_positon_tag))
 
    if len(five_list) < samples:
        return five_list
    else:
        return five_list[:samples]
        
def create_df(all_samples):
    features = list(set([y for y, _ in all_samples])) + list(set([i for _, sample in all_samples for i in sample ])) 
    nw_dict = {}
    for i in range(len(all_samples)):
        list_template = [0 for x in range(len(features))]
        key, letters = all_samples[i]
        for letter in letters + [key]:
            position = features.index(letter)
            list_template[position] = 1
        nw_dict[tuple(letters)] = list_template    

    df = pd.DataFrame(nw_dict, index = features).T

    # Assuming only predicting Verb class
    final_df = df.drop(['JJ', 'NN', 'RB'], axis=1)
    return final_df

def split_samples(fulldf, test_percent=20):
    rows = fulldf.shape[0]
    rowdata = []
    for i in range(rows):
        rowdata.append(fulldf.iloc[i, 1:].tolist())
    label = fulldf.iloc[:, 0].tolist()
    # Just use the split from sklearn
    X_train, X_test, y_train, y_test = train_test_split(rowdata, label,
                                                        test_size=test_percent*0.01)
    return X_train, y_train, X_test, y_test
    
def train(X_train, y_train, kernel):
    if kernel == 'linear':
        linear = svm.SVC(kernel='linear', C=1, decision_function_shape='ovo').fit(X_train, y_train)
        return linear
    elif kernel == 'rbf':
        rbf = svm.SVC(kernel='rbf', gamma=1, C=1, decision_function_shape='ovo').fit(X_train, y_train)
        return rbf
    else:
        print("This kernel is not supported yet!")
    
def eval_model(model, test_X, test_y):
    pridicted_y = model.predict(test_X)
    scores = metrics.classification_report(test_y, pridicted_y)
    print(scores)
