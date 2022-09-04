# News title cluster

### Note:

  ```
  python 
  ```


## Model src:
- word vetcor：
    -(向量模型)[http://nlp.tmu.edu.tw/word2vec/index.html]
- 斷詞：
    - jieba.set_dictionary('models/dict.txt.big.txt')
    - https://github.com/fxsjy/jieba

## API開發:
-

## Quick Start:
(1) Init: 
pip install -r requirements.txt

(2) Run example.
python example.py


## output

company_title_cluster_findk.csv
'''
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
'''

'''
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
'''

## update
1.使用金融向量
2.斷詞優化
3.模型優化
       
