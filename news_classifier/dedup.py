
def init():
    """ Create an object and init it. Make it as a function as we may need to config something."""
    c = NewsDeduper()

    return c


class NewsDeduper():
    """ Dedup news. 
        假設輸入為 "同一間公司" 的 N則新聞
        每則新聞包含 "Title", "Text"
        辨識出明顯相同的新聞
    
    """

    def __init__(self):
        pass


    def dedup(self, news_list):
        """
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
        
        Returns
        -------
        list of {news}
            news_list with groupid column inserted.
            {
            'Title': 'Title of the news',
            'Content': 'Content of the news',
            'Media': 'Source of the news',
            'gid': int, identical news will have the same id.
            }            
        """
        titles = {}
        for news in news_list:
            # FIXME: 去除明顯重複的新聞
            # 以下亂寫的，請重新Implement
            # 假設Title 格式為 "新聞Title - Source"
            grps = news['Title'].split("-")
            t_key = grps[0]
            if t_key in titles:
                gid = titles[t_key]
            else:
                gid = len(titles) + 1
                titles[t_key] = gid

            news['gid'] = gid
        
        # sort results by gid
        news_list = sorted(news_list, key=lambda x: x['gid'])
        return news_list
    


