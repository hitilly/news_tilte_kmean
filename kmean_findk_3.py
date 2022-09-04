# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 15:22:54 2022

@author: user
"""


import gensim
from gensim.models.word2vec import Word2Vec
model = gensim.models.KeyedVectors.load_word2vec_format('models/tmunlp_1.6B_WB_50dim_2020v1.bin', 
                                                        unicode_errors='ignore', 
                                                        binary=True)
#https://www.nltk.org/_modules/nltk/cluster/kmeans.html
#https://blog.csdn.net/ling620/article/details/99441942
#模型下載
#http://nlp.tmu.edu.tw/word2vec/index.html
#%%
from nltk.cluster import KMeansClusterer
import nltk
import numpy as np
import jieba,re
stopwords = [line.strip() for line in open('models/stopwords',encoding='UTF-8').readlines()]

jieba.set_dictionary('models/dict.txt.big.txt')
def get_vector(news_list):
       news_list_vectors=[]
       for news in news_list:
           
            grps = news['Title'].split("-")
            t_key = grps[0]
            t_key = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（ )《 》]", "",t_key)
            #t_key = re.sub(r'[^\u4e00-\u9fa5]+','',t_key)
            if len(t_key) !=0:
                sum_vc=0
                len_word=0
                sentence_depart = jieba.cut(t_key.strip())
               # print('sentence_depart',sentence_depart)
                for word in sentence_depart:
                    if word not in stopwords:
                       # print(word)
                        try:
                            w2v=model[word]
    
                        except KeyError:  
                            w2v=np.zeros(50)
                        sum_vc=sum_vc+w2v
                        len_word = len_word+1
                mean_vc = sum_vc/len_word+0.001

                   #v = sum([embeddings_index.get(w,np.zeros((100,))) for w in t_key.split()])/len(t_key.split())+0.001
                   #print("mean_vc=",mean_vc)
            else :
                    mean_vc = np.zeros((50,))
            news_list_vectors.append(mean_vc)   
       return news_list_vectors
             
#http://blog.itpub.net/31562039/viewspace-2286669/             
 
from sklearn import cluster
from sklearn import metrics
import re
from sklearn.manifold import TSNE         
'''
def news_kmeans(X,n): 

       from sklearn.metrics import silhouette_score      
       NUM_CLUSTERS=n
       kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats=10,avoid_empty_clusters=True)
     
       assigned_clusters = kclusterer.cluster(X, assign_clusters=True)
       #print("estimator.inertia_",assigned_clusters.inertia_)
       #print('labels_',kclusterer.labels_)
       if len(np.unique(assigned_clusters))>1:
            sc_score = metrics.silhouette_score(X,assigned_clusters\
                                ,sample_size=None, metric='euclidean')#'euclidean')
            sc_scores.append(sc_score)
       return assigned_clusters
'''
     
#https://github.com/cr0hn/UnderFucking/blob/master/thirdparty_libs/nltk/cluster/kmeans.py
#https://www.nltk.org/_modules/nltk/cluster/kmeans.html
#https://www.csdn.net/tags/MtTaMgzsNDYyMzA5LWJsb2cO0O0O.html
#from news_classifier import glove_vec
#创建空列表，依次创建k=1~15的模型并 保存SSE结果
def find_k(X,n):
    import matplotlib.pyplot as plt
    from sklearn.datasets import make_blobs
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
    clusters = range(2,n)
    print('num clusters',clusters)
    sc_scores = []
    scores_dict={}
    assigned_clusters_dict={}
    for k in clusters:  
        kmeans_model = KMeans(n_clusters=k).fit(X)
        
        print('k',k)
        #kmeans_model = KMeansClusterer(n, distance=nltk.cluster.util.cosine_distance, repeats=10,avoid_empty_clusters=True)
        assigned_clusters =kmeans_model.labels_
        #assigned_clusters = kmeans_model.cluster(X, assign_clusters=True)
        print('kmeans_model.labels_=',kmeans_model.labels_)
        
        print('np.unique(km.labels_)',np.unique(assigned_clusters))
        print('assigned_clusters',assigned_clusters)
        if len(np.unique(assigned_clusters))>1:
            sc_score = metrics.silhouette_score(X,assigned_clusters\
                                ,sample_size=None, metric='euclidean')#'euclidean')
            sc_scores.append(sc_score)
            scores_dict[k]=sc_scores
            assigned_clusters_dict[k]=assigned_clusters
            
            print(sc_scores)
                    
            # plt.figure()
            # plt.plot(clusters, sc_scores, 'bx-')
            # plt.rcParams['figure.figsize'] = [12,8]
            # plt.xlabel('分群数量',fontsize=18)
            # plt.ylabel('Silhouette Coefficient Score',fontsize=18)  #样本平均轮廓系数
            # plt.xticks(fontsize=15)
            # plt.yticks(fontsize=15)
            # plt.show()
            #print('np.max(sc_scores)=',np.max(sc_scores))
            
            #print(max(scores_dict.items(), key = lambda k : k[1]))
            #return max(scores_dict, key=scores_dict.get)
        else: 
            print('same class',assigned_clusters)
            return assigned_clusters
        
        print('max(scores_dict, key=scores_dict.get)', max(scores_dict, key=scores_dict.get))
        
        print(max(scores_dict.items(), key = lambda k : k[1]))
        print('assigned_clusters',assigned_clusters_dict[max(scores_dict, key=scores_dict.get)])
    return assigned_clusters_dict[max(scores_dict, key=scores_dict.get)]
    # #作出K—平均轮廓系数曲线
    # plt.figure()
    # plt.plot(clusters, sc_scores, 'bx-')
    # plt.rcParams['figure.figsize'] = [12,8]
    # plt.xlabel('分群数量',fontsize=18)
    # plt.ylabel('Silhouette Coefficient Score',fontsize=18)  #样本平均轮廓系数
    # plt.xticks(fontsize=15)
    # plt.yticks(fontsize=15)
    # plt.show()
    # print('np.max(sc_scores)=',np.max(sc_scores))
    
    # print(max(scores_dict.items(), key = lambda k : k[1]))
    # print("max(stats, key=stats.get)",max(scores_dict, key=scores_dict.get))
    # return max(scores_dict, key=scores_dict.get)

import time
import os,csv
       
CSVFILE = r"news_samples/dedup_sample.csv"

#deduper = dedup.init()

# Parse News from a CSV file 

with open(CSVFILE, encoding='Big5') as rf:
    reader = csv.DictReader(rf)
    news_by_company = {}
    for row in reader:
        # 先依照公司分類
        target = row['id']
        news = {
            "Title": row['Title'],
            "Content": row['Content'],
            "Media": row['Media'],
        }
        if target not in news_by_company:
            news_by_company[target] = []

        # Save for later output:
        news_by_company[target].append(news)
    
print("# Total ids:", len(news_by_company))
#print("news_by_company=",news_by_company)
print("news_by_company.items()=",news_by_company.keys())  


'''
        Parameters
        ----------
        news_list: list of news: list of news
            newslist = [{
                'Title': 'Title of the news',
                'Content': 'Content of the news',
                'Media': 'Source of the news',
            },
            ...
        ]

'''
'''
newlists={'aa':[{'Title':'33'}]}
news_by_company={'aa':[{'Title':'台積電失守500元！台股午盤跌310點','Content': 'nun','Media': 'Source of the news'},
          {'Title': '台積電失守500元', 'Content': 'nun','Media': 'Source of the news'},
          {'Title': '台積電失守500元呢', 'Content': 'nun','Media': 'Source of the news'},
          {'Title': '台股午盤跌310點', 'Content': 'nun','Media': 'Source of the news',}, 
          {'Title': '4張台積電全賣！「虧損130萬元」認賠出場　他PO畢業文：專心工作','Content': 'nun','Media': 'Source of the news',},
          {'Title': '台積電（2330）今天失守500元大關','Content': 'nun','Media': 'Source of the news', },
          {'Title': '英特爾晶片遲到 台積電3奈米擴產恐踩煞車','Content': 'nun', 'Media': 'Source of the news',},
          {'Title': '台積電3奈米擴產放緩？傳被英特爾晶片遲到拖累','Content': 'nun','Media': 'Source of the news',},
          {'Title': '台積電ADR2日下跌0.74美元跌幅0.91%折台股494.91元','Content': 'nun','Media': 'Source of the news',},
          {'Title': '台積電ADR2美元跌幅0.91%','Content': 'nun','Media': 'Source of the news',}]
                 
                 
                 }

'''
#台積電ADR2日下跌0.74美元跌幅0.91%折台股494.91元
#news_by_company.items()= dict_keys(['中華電', '世界', '台積電', '長榮', '國泰金', '富邦金', '惠特', '貿聯-KY', '陽明', '萬海', '聯發科', '聯電', '台塑', '台灣大', '定穎', '統一', '微星'])   
#%%
import re

import re
company=dict()

import pandas as pd
cluster_list=[]
company_list=[]
title_list=[]
for key,val in news_by_company.items():
    

   # my_dataframe['company_name'].append(key)
    print("# Grouped result:", key)
    #print('val',len(val))
    company[key] =[]
    #results = deduper.dedup(val)
    vector_company = get_vector(val)
        

    if len(val)==1:
        assigned_clusters=[0]
    else:
        assigned_clusters = find_k(np.array(vector_company),len(val))   

   # assigned_clusters =news_kmeans(np.array(vector_company),best_k)
    kclusterer = dict()
    
    for j in range(len(val)):
        print(" ",assigned_clusters[j],' ', val[j]['Title'])
        cluster_list.append(assigned_clusters[j])
        title_list.append(val[j]['Title'])
        company_list.append(key)

df = pd.DataFrame(list(zip(company_list, title_list,cluster_list)),
               columns =['company','Title', 'cluster'])

# Using groupby & sort_values to sort.
df_sort=df.sort_values(['company','cluster'],ascending=True)
print(df_sort)
df_sort.to_csv('company_title_cluster_findk.csv')

#%% 
#相關閱讀
 #https://medium.com/@derekliao_62575/%E7%89%A9%E4%BB%A5%E9%A1%9E%E8%81%9A-%E6%96%87%E5%AD%97%E4%B9%9F%E6%98%AF-%E6%96%87%E6%9C%AC%E8%81%9A%E9%A1%9E%E5%88%86%E6%9E%90-clustering-f95f6c0cedaf
 #中文w2v vocab 的 encoding 無法使用
 #https://github.com/mymagicpower/AIAS/blob/main/2_nlp_sdks/embedding/word_encoder_cn_sdk/README.md