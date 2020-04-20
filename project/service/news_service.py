from db.news_dao import NewsDao

class NewsService:
    __news_dao = NewsDao()
    # 获取审批新闻列表
    def search_unreview_list(self, page):
        result = self.__news_dao.search_unreview_list(page)
        return result

    # 获取审批新闻总页数
    def search_unreview_count_page(self):
        count_page = self.__news_dao.search_unreview_count_page()
        return count_page

    # 审批新闻
    def update(self, news_id):
        self.__news_dao.update(news_id)

    # 获取新闻列表
    def search_list(self, page):
        result = self.__news_dao.search_list(page)
        return result

    # 获取新闻总页数
    def search_count_page(self):
        count_page = self.__news_dao.search_count_page()
        return count_page

    # 删除新闻
    def delete(self, news_id):
        self.__news_dao.delete(news_id)