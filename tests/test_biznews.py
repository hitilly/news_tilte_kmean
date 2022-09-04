# -*- coding: utf-8 -*-

#from .context import aistm
import unittest

from news_classifier import biznews

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        self.nreader = biznews.init()
        self.keywords = ['入獄', '上訴', '貪汙', '大跌', '跌停']
        self.title = '王小明否認貪汙。王: 上訴中，我沒收現金，只是剛好買到漲價的股票，不是貪汙，都是網軍攻擊抹黑。'
        self.body = """ 
         潤泰全、潤泰新爆淨值大幅減損危機，股價連二日跌停，更傳言遭股市禿鷹襲擊，證期局副局長張子敏昨（21）日指出，臺灣證券交易所已將潤泰雙雄列為「線上監視股票」，目前正在監視中，股市本就有監視制度，對有價證券執行監視查核，若有不法情事，就會依規定辦理，維護投資大眾權益。

資深市場人士則分析，以7月來兩檔個股借券賣出、融券等數據來看，這兩檔個股並未有異常之處，待疑慮釐清後，股價自然回歸基本面。
        """

    def test_class_init(self):
        self.assertIsNotNone(self.nreader)
        self.assertTrue(len(self.nreader.nn_keywords) > 0, "No NN keywords loaded")


    def test_classify_return_format(self):
        """ Test the return format of the class.
            The result is a dictionary with format like:
                result = {
                    'NN': nn_flag,
                    'NN_SCORE': nn_score,
                    'NN_KEYWORDS': nn_tokens,
                    'ESG': esg_flag,
                    'ESG_SCORE': esg_score,
                }
        """
        news_title = "this is a title"
        news_body = "this is news body"
        return_keys = ['NN', 'NN_SCORE', 'NN_KEYWORDS', 'ESG', 'ESG_SCORE', 'ESG_KEYWORDS']

        result = self.nreader.classify(news_title, news_body)
        for k in return_keys:
            self.assertTrue( k in result, "Key '{}' not found in the classify return!".format(k))

    def test_find_keywords(self):

        cnt_drafts, matched_keywords, total_cnt = self.nreader.find_keywords(
            self.title, self.keywords)

        self.assertEqual(matched_keywords, ['貪汙', '上訴'])
        self.assertEqual(total_cnt, 3)
        self.assertEqual(cnt_drafts, [('貪汙', 2), ('上訴', 1)])

    def test_evaluate(self):

        score, keywords = self.nreader.evaluate(self.title, self.body, self.keywords)

        self.assertGreater(score, 0)
        self.assertEqual(keywords,  ['貪汙', '上訴','跌停'])

if __name__ == '__main__':
    unittest.main()