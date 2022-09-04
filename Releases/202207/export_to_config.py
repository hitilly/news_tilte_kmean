# -*- coding: utf-8 -*-
# Export excel files to config file
import pandas as pd

CONFIG_FN = '../../news_classifier/config_202207.py'
NN_FN = 'keywords_nn_v202207.xlsx'
ESG_FN = 'keywords_esg_v202207.xlsx'


## Load nn/esg keywords from excel
dfnn = pd.read_excel(NN_FN)
nnlist = list(dfnn[dfnn['Selected'] == 1]['Keyword'])
dfesg = pd.read_excel(ESG_FN)
esglist = list(dfesg[dfesg['Selected'] == 1]['Keyword'])

print("# Exporting NN keywords", nnlist)
print("# Exporting ESG keywords", esglist)


## Format output list to str
def printlist(wordlist, max_per_line):
    outstr = ""
    for i in range(len(wordlist)):
        if i % max_per_line == 0: outstr += "\n"
        outstr += "'{}',".format(wordlist[i])
    return outstr


## Export to config.py
f_conf = open(CONFIG_FN, 'w')
f_conf.write("""# -*- coding: utf-8 -*-

# NN Keywords
NN_KEYWORDS = [ """)
f_conf.write(printlist(nnlist, 10))
f_conf.write("""]

# ESG Keywords
ESG_KEYWORDS = [ """)
f_conf.write(printlist(esglist, 10))
f_conf.write("]\n")
f_conf.close()