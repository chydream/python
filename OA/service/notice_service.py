from db.notice_dao import NoticeDao

class NoticeService:
    __notice_dao = NoticeDao()
    # 添加通知公告信息
    def notice_add(self, username, title, content):
        self.__notice_dao.notice_add(username, title, content)

    # 获取通知公告信息列表分页
    def get_list(self, page, username):
        result = self.__notice_dao.get_list(page, username)
        return result

    # 获取总页数
    def get_total_page(self):
        result = self.__notice_dao.get_total_page()
        return result

    # 修改通知公告信息
    def notice_update(self, username, title, content, id):
        self.__notice_dao.notice_update(username, title, content, id)

    # 删除通知公告
    def notice_delete(self, id):
        self.__notice_dao.notice_delete(id)

    # 查看通知公告信息
    def notice_view(self, id):
        result = self.__notice_dao.notice_view(id)
        return result