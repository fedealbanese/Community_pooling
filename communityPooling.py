# -*- coding: utf-8 -*-
"""
@author: Federico Albanese
"""
import pandas as pd
import numpy as np
import networkx as nx
import community as community_louvain #https://github.com/taynaud/python-louvain

np.random.seed(123) #Reproducibility

data = pd.read_csv("data.csv")
"""
Dataframe with one tweet per row. The necesary collumns are the following:
user_Id: [int] the id of the user that creat the tweet.
is_RT: [bool] True if the tweet is a retweet and False in case it is not.
user_Id_RT: the id of the user that creat the tweet. NaN in case it is not a RT
text:[str] the text of the tweet.
"""
train_size = 0.8
data["train/test"] = [0]*int(data.shape[0]*train_size) + [1]*(data.shape[0] - int(data.shape[0]*train_size))
data_train = data[(data["train/test"] == 0)]

G = nx.Graph()
for i in range(data_train.shape[0]):
    if data_train.is_RT.iloc[i]:
        nodo1 = int(data_train.user_Id.iloc[i])
        nodo2 = int(data_train.user_Id_RT.iloc[i])
        if (nodo1, nodo2) in G.edges:
            G.edges[nodo1, nodo2]['weight'] += 1
        else:
            G.add_edge(nodo1, nodo2, weight=1)
    else:
    	G.add_node(int(data_train.user_Id.iloc[i]))
            

partition = community_louvain.best_partition(G) 

clusters =  np.zeros(data_train.shape[0])

for i in range(data_train.shape[0]):
    cluster = partition[data_train.iloc[i].user_Id]
    clusters[i] = cluster
    
data_train["user_Community"] = clusters

documents = []
for community in data_train["user_Community"].unique(): 
    documents.append(data_train[data_train.user_Community == com].text.str.cat(sep = ". "))