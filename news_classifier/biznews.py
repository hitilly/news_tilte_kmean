from numpy import mat
# from news_classifier import config
from news_classifier import config_202207 as config

def init():
    """ Create an object and init it. Make it as a function as we may need to config something."""
    c = NewsReader()

    # Note: keywords are now load from config directly.
    # This is just a place holder reserved for future.   
    c.load_NN_keywords("")
    return c

class NewsReader():
    """ News Classifier for Business related news."""

    def __init__(self):
        self.nn_keywords = config.NN_KEYWORDS
        self.esg_keywords = config.ESG_KEYWORDS
        
        # Scoring functions parameters
        self.title_weight = 0.3
        self.body_weight = 0.1

    def load_NN_keywords(self, filepath):
        """Load (user defined) NN Keywords from config file"""
        # Place holder, not required now.
        pass

    def classify(self, news_title, news_body):
        """Gets and prints the spreadsheet's header columns

        Parameters
        ----------
        news_title: str
            The title of the news as a string.
        news_body: str
            The content of the news as a string.

        Returns
        -------
        dict
            News classify result. 
        """

        nn_flag = False
        nn_score = 0
        nn_tokens = []

        esg_flag = False
        esg_score = 0
        esg_tokens = []

        nn_score, nn_tokens = self.evaluate(news_title, news_body, self.nn_keywords)
        if len(nn_tokens) > 0: 
            nn_flag = True

        esg_score, esg_tokens = self.evaluate(news_title, news_body, self.esg_keywords)
        if len(esg_tokens) > 0:
            esg_flag = True
        

        result = {
            'NN': nn_flag,
            'NN_SCORE': nn_score,
            'NN_KEYWORDS': nn_tokens,
            'ESG': esg_flag,
            'ESG_SCORE': esg_score,
            'ESG_KEYWORDS': esg_tokens,
        }
        return result

    def evaluate(self, news_title, news_body, keywords):
        """Find matched keywords and calculate score.
        
        Parameters
        ----------
        news_title: str
            The title of the news as a string.
        news_body: str
            The content of the news as a string.
        keywords: [str]
            NN/ESG Keywords

        Returns
        -------
        float:
            Score
        [str]:
            List of matched keywords (sorted by cnt) 
        """

        debug = list()

        """ Keywords Matching """
        keywords_dict = {}

        ## news_title
        title_keyword_index, title_matched_keywords, title_total_cnt = self.find_keywords(news_title, keywords)
        
        ## news_body
        body_total_cnt = 0
        body_keyword_index, body_matched_keywords, body_total_cnt = self.find_keywords(news_body, keywords)
        
        # Merge keywords dictionary and sort by cnt
        for (key, cnt) in title_keyword_index + body_keyword_index:
            if key not in keywords_dict:
                keywords_dict[key] = cnt
            else:
                keywords_dict[key] += cnt

        keywords_dict = dict(sorted(keywords_dict.items(), key=lambda item: item[1], reverse = True))
        matched_keywords = list(keywords_dict.keys())

        """ Scoring """
        weight = round(self.title_weight / self.body_weight, 2)
        matched_keywords_cnt = weight * title_total_cnt + body_total_cnt
        
        if matched_keywords_cnt == 0:
            score = 0.00
        score = 0.50 + 0.50 / (15 ** 2) * (matched_keywords_cnt) ** 2
        score = round(score, 2) if score <= 1.00 else 1.00

        if (len(matched_keywords)) == 0:
            score = 0
            
        return round(score, 2), matched_keywords


    def find_keywords(self, text, keywords):
        """Details of finding keywords.

        Parameters
        ----------
        text: str
            Input text.
        keywords: list of string
            Target (NN/ESG) keywords.

        Returns
        -------
        details, matched keywords, countß
            rtype1: list of Tuple[str, int]
            rtype2: list of string
            rtype3: integer
        """
        cnt_drafts = list()
        for word in keywords:
            cnt = text.count(word)
            if cnt > 0:
                cnt_drafts.append((word, cnt))

        cnt_drafts = sorted(cnt_drafts, key=lambda x: (x[1]), reverse=True)
        matched_keywords = [cnt[0] for cnt in cnt_drafts]
        total_cnt = sum([cnt[1] for cnt in cnt_drafts])
        return cnt_drafts, matched_keywords, total_cnt
