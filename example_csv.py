from news_classifier import biznews

import os, csv
CSVFILE = r"news_samples/NewsData.csv"

nreader = biznews.init()

newsdata = []
results = []
# Parse News from a CSV file 
with open(CSVFILE, encoding='Big5') as rf:
    reader = csv.DictReader(rf)
    for row in reader:
         news_title = row['Title']
         news_body = row['Content']

         # News Classify
         result = nreader.classify(news_title, news_body)
         
         # Save for later output:
         newsdata.append((news_title, news_body))
         results.append(result)

print("# Total News:", len(results))
print("#   Example results from the last 20 news:")
for i in range(len(results)-20, len(results)):
    print(newsdata[i][0])
    print(results[i])
