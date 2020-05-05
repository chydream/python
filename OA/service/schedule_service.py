from db.schedule_dao import ScheduleDao

class SchedulService:
    __schedule_dao = ScheduleDao()
    # 添加日程信息
    def schedule_add(self, username, year, month, day, plan):
        self.__schedule_dao.schedule_add(username, year, month, day, plan)

    # 获取日程信息列表分页
    def get_list(self, page, username, role):
        result = self.__schedule_dao.get_list(page, username, role)
        return result

    # 获取总页数
    def get_total_page(self):
        result = self.__schedule_dao.get_total_page()
        return result

    # 修改日程信息
    def schedule_update(self, year, month, day, plan, id):
        self.__schedule_dao.schedule_update(year, month, day, plan, id)

    # 删除日程
    def schedule_delete(self, id):
        self.__schedule_dao.schedule_delete(id)

    # 查看日程信息
    def schedule_view(self, id):
        result = self.__schedule_dao.schedule_view(id)
        return result