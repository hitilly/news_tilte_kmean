from news_classifier import dedup

import os, csv
CSVFILE = r"news_samples/dedup_sample.csv"

deduper = dedup.init()

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

for key,val in news_by_company.items():
    print("# Grouped result:", key)
    results = deduper.dedup(val)

    print("#   Grouping results:")
    gid = 0
    for news in results:
        newid = news['gid']
        ident = "  "
        if newid > gid:
            ident = ""
            gid = newid
        print("{}[{}], {}".format(ident, news['gid'], news['Title']))

    print("")