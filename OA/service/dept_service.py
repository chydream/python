from db.dept_dao import DeptDao

class DeptService:
    __dept_dao = DeptDao()
    # 获取部门列表
    def get_list(self):
        result = self.__dept_dao.get_list()
        return result