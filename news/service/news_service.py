from news.db.news_dao import NewsDao

class NewsService:
    __news_dao = NewsDao()

    # 查询待审批新闻列表
    def search_unreview_list(self, page, page_size):
        result = self.__news_dao.search_unreview_list(page, page_size)
        return result

    def search_unreview_count_page(self):
        count_page = self.__news_dao.search_unreview_count_page()
        return count_page

    def update_unreview_news(self, id):
        self.__news_dao.update_unreview_news(id)

    # 查询新闻列表
    def search_list(self, page, page_size):
        result = self.__news_dao.search_list(page, page_size)
        return result

    def search_count_page(self):
        count_page = self.__news_dao.search_count_page()
        return count_page

    def delete_by_id(self, id):
        self.__news_dao.delete_by_id(id)