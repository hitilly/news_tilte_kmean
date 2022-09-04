## Simple script to expand the nn/esg keywords

import pandas as pd
from news_classifier import config
from news_classifier.w2vhelper import w2v

## Configs:
FN_NN = 'tmp/keywords_nn_draft.xlsx'
FN_ESG = 'tmp/keywords_esg_draft.xlsx'
FN_model = 'models/merge_sgns_bigram_char300.txt.bz2'

# Load model
w2v = w2v()
w2v.load_model(FN_model)

# Expand keywords 
nndata = w2v.extend_keywords(config.NN_KEYWORDS)
esgdata = w2v.extend_keywords(config.ESG_KEYWORDS)

# Export to excel
dfnn=pd.DataFrame(nndata)
dfnn.to_excel(FN_NN, index=False)
print("NN Extended: {} ({} => {})".format(FN_NN, len(config.NN_KEYWORDS), dfnn.shape[0]))      
    
dfesg=pd.DataFrame(esgdata)
dfesg.to_excel(FN_ESG, index=False)
print("ESG Extended: {} ({} => {})".format(FN_ESG, len(config.ESG_KEYWORDS), dfesg.shape[0]))