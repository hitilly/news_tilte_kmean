# News title cluster

## Model src:
- word vetcor：
    -(向量模型)[http://nlp.tmu.edu.tw/word2vec/index.html]
- 斷詞：
    - jieba.set_dictionary('models/dict.txt.big.txt')
    - https://github.com/fxsjy/jieba

## 流程
- title轉為詞向量並斷詞   
- 輸入kmean模型   
- 依照輪廓分數決定類別數   
   - 聚类结果的轮廓系数的取值在【-1,1】之间，值越大，说明同类样本相距约近，不同样本相距越远，则聚类效果越好. 
   - https://blog.csdn.net/maple05/article/details/110454075
   - https://zhuanlan.zhihu.com/p/51777857
   - 
## run:
(1) Init: 
pip install -r requirements.txt（未更新）

(2) Run example.
python kmean_findk_3.py


## output

(1) 新聞聚類結果
company_title_cluster_findk.csv

,company,    Title,                                  cluster
5,世界,流動性困難英連鎖影院電影世界考慮在美聲請破產| 聯合新聞網 - udn.com,0  
7,世界,流動性困難英連鎖影院電影世界考慮在美聲請破產| 聯合新聞網 - udn.com,0  
8,世界,國際宗教信仰迫害受難者紀念日 民團談太極門案法稅貪腐 - 中時新聞網 Chinatimes.com,0  
10,世界,流動性困難英連鎖影院電影世界考慮在美聲請破產| 聯合新聞網 - udn.com,0  
11,世界,國際宗教信仰迫害受難者紀念日 民團談太極門案法稅貪腐 - 中時新聞網 Chinatimes.com,0  
13,世界,流動性困難英連鎖影院電影世界考慮在美聲請破產| 聯合新聞網 - udn.com,0  
14,世界,國際宗教信仰迫害受難者紀念日 民團談太極門案法稅貪腐 - 中時新聞網 Chinatimes.com,0  
4,世界,乾旱加缺電 中國大陸米、鋁、鋰、銅、矽生產備受威脅 - udn.com,1   
6,世界,乾旱加缺電 中國大陸米、鋁、鋰、銅、矽生產備受威脅 - udn.com,1  
9,世界,乾旱加缺電 中國大陸米、鋁、鋰、銅、矽生產備受威脅 - udn.com,1  
12,世界,乾旱加缺電 中國大陸米、鋁、鋰、銅、矽生產備受威脅 - udn.com,1  
0,中華電,《美股掃瞄》內外夾擊 美股重挫、費半崩跌近4%(2-2) - 中時新聞網 Chinatimes.com,0  
1,中華電,《美股掃瞄》內外夾擊 美股重挫、費半崩跌近4%(2-2) - 中時新聞網 Chinatimes.com,0   
2,中華電,《美股掃瞄》內外夾擊 美股重挫、費半崩跌近4%(2-2) - 中時新聞網 Chinatimes.com,0  
3,中華電,《美股掃瞄》內外夾擊 美股重挫、費半崩跌近4%(2-2) - 中時新聞網 Chinatimes.com,0  

(2) 測試結果
company_title_cluster_findk_test.csv
,company,      Title,                           cluster  
4,aa,4張台積電全賣！「虧損130萬元」認賠出場　他PO畢業文：專心工作,0  
6,aa,英特爾晶片遲到 台積電3奈米擴產恐踩煞車,0  
7,aa,台積電3奈米擴產放緩？傳被英特爾晶片遲到拖累,0  
0,aa,台積電失守500元！台股午盤跌310點,1  
1,aa,台積電失守500元,1  
2,aa,台積電失守500元呢,1  
3,aa,台股午盤跌310點,1  
5,aa,台積電（2330）今天失守500元大關,1  
8,aa,台積電ADR2日下跌0.74美元跌幅0.91%折台股494.91元,1  
9,aa,台積電ADR2美元跌幅0.91%,1  


## update
1.使用金融向量
 - https://github.com/Embedding/Chinese-Word-Vectors
2.斷詞優化  
3.模型優化  
 - nltk kmean
   - 無法使用輪廓係數計算聚類數量   
   - http://cobweb.cs.uga.edu/~jam/scalation_1.5/scalation_modeling/target/scala-2.12/api/scalation/analytics/clusterer/KMeansClusterer.html
   - https://stackoverflow.com/questions/59549953/get-inertia-for-nltk-k-means-clustering-using-cosine-similarity
 - lda
    - https://github.com/YangBin1729/nlp_notes/blob/master/06-%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86/09-LDA%E4%B8%BB%E9%A2%98%E6%A8%A1%E5%9E%8B.ipynb       
       
 https://tedboy.github.io/nlps/generated/nltk.cluster.html
 。
