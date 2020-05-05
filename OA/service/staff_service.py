from db.staff_dao import StaffDao

class StaffService:
    __staff_dao = StaffDao()
    # 添加职工信息
    def staff_add(self, truename, email, sex, deptno, job, phone, address):
        self.__staff_dao.staff_add(truename, email, sex, deptno, job, phone, address)

    # 获取职工信息列表分页
    def get_list(self, page):
        result = self.__staff_dao.get_list(page)
        return result

    # 获取总页数
    def get_total_page(self):
        result = self.__staff_dao.get_total_page()
        return result

    # 修改职工信息
    def staff_update(self, deptno, job, phone, address, id):
        self.__staff_dao.staff_update(deptno, job, phone, address, id)

    # 删除职工
    def staff_delete(self, id):
        self.__staff_dao.staff_delete(id)

    # 查看职工信息
    def staff_view(self, email):
        result = self.__staff_dao.staff_view(email)
        return result