from db.news_dao import NewsDao
from db.redis_news_dao import RedisNewsDao
from db.mongo_news_dao import MongoNewsDao

class NewsService:
    __news_dao = NewsDao()
    __redis_news_dao = RedisNewsDao()
    __mongo_news_dao = MongoNewsDao()
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
        content_id = self.__news_dao.search_contentid(news_id)
        self.__mongo_news_dao.delete(content_id)
        self.__news_dao.delete(news_id)

    # 发表新闻
    def insert(self, title, editor_id, type_id, content, is_top):
        self.__mongo_news_dao.insert(title, content)
        content_id = self.__mongo_news_dao.search_content_id(title)
        self.__news_dao.insert(title, editor_id, type_id, str(content_id), is_top)

    # 获取新闻信息
    def search_news_by_id(self, id):
        result = self.__news_dao.search_news_by_id(id)
        return result

    # 添加新闻缓存数据
    def insert_cache(self, id, title, username, type, content_id, is_top, create_time):
        content = self.__mongo_news_dao.search_content(content_id)
        self.__redis_news_dao.insert_cache(id, title, username, type, content, is_top, create_time)

    # 编辑新闻
    def update_news_by_id(self, id, title, type_id, content, is_top, content_id):
        self.__mongo_news_dao.update_content(content_id, title, content)
        self.__news_dao.update_news_by_id(id, title, type_id, content_id, is_top)

    # 删除新闻缓存数据
    def delete_cache(self, id):
        self.__redis_news_dao.delete_cache(id)
