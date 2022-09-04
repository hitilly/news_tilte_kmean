## Helper functions
from opencc import OpenCC
from gensim.models.keyedvectors import KeyedVectors

class w2v():
    def __init__(self):
        self.cct2s = OpenCC('t2s') 
        self.ccs2t = OpenCC('s2t')
        
        # generate top N with most_similar()
        self.topN = 5
        # cutoff score
        self.cutoff = 0.6
        # 預設w2v model為簡體中文
        self.lang = 'zh-cn' 
        
    def load_model(self, modelfn):
        self.model = KeyedVectors.load_word2vec_format(modelfn,
                                          binary=False, 
                                          unicode_errors='ignore')
        print(modelfn, "loaded")

    def most_similar(self, term, n = None, cutoff = None):
        if n is None:
            n = self.topN
        if cutoff is None:
            cutoff = self.cutoff
        # Generate top N similar terms
        
        # 預設輸入為zh-tw, 模型為zh-cn
        if self.lang == 'zh-cn':
            term = self.cct2s.convert(term)
        
        try:
            drafts = self.model.most_similar(term, topn = n)
        except:
            print("OOV", term)
            drafts = []
        
        # 轉回繁體
        results = []
        for (word, score) in drafts:      
            if self.lang == 'zh-cn':
                word = self.ccs2t.convert(word)
            if score >= cutoff:
                results.append((word, score))
        return results

    ## Get Vector of a key
    def get_vector(self, wordtw):
        wordcn = self.cct2s.convert(wordtw)
        try:
            vec = self.model.get_vector(wordcn)
        except:
            vec = None
        return vec

    ##  Expand keyword list
    def extend_keywords(self, wordlist):
        data = []
        known = [] + wordlist
        wordRoot = {}

        for w in wordlist:    
            for (word, score) in self.most_similar(w):
                # 記錄新生成的詞彙的Root.
                if word not in wordRoot:
                    wordRoot[word] = []    
                wordRoot[word].append(w)
                
                ## 排除以下情況
                ignore = False
                # 1. 至少兩個字, e.g. 偷盜(O), 偷(X)
                if len(word) < 2: ignore = True
                # 1. 該詞彙已經出現過 (原本Seed or 新生成的詞彙中)
                if word in known: ignore = True
                # 2. 爆炸 -(擴展)-> 發生爆炸 
                for substr in known:
                    if substr in word:
                        ignore = True
                        
                if not ignore:
                    known.append(word)
                    
                    
        # 產出合併清單
        for word in known:
            if word in wordlist:
                row = {'Keyword': word, 'Seed': 1, 'From': "", 'Selected': 1 , 
                       'Vector': self.get_vector(word)}
            else:
                row = {'Keyword': word, 'Seed': 0, 'From': ','.join(wordRoot[word]), 'Selected': 0, 
                       'Vector': self.get_vector(word)}
            data.append(row)                                  
        return data