from db.file_dao import FileDao
from db.mongo_file_dao import MongoFileDao

class FileService:
    __file_dao = FileDao()
    __mongo_file_dao = MongoFileDao()
    # 添加文件信息
    def file_add(self, username, filename, filesize, fileinfo, file_id):
        self.__file_dao.file_add(username, filename, filesize, str(fileinfo), file_id)

    # 获取文件信息列表分页
    def get_list(self, page, username, role):
        result = self.__file_dao.get_list(page, username, role)
        return result

    # 获取总页数
    def get_total_page(self):
        result = self.__file_dao.get_total_page()
        return result

    # 修改文件信息
    def file_update(self, username, filename, filesize, fileinfo, id):
        self.__file_dao.file_update(username, filename, filesize, fileinfo, id)

    # 删除文件
    def file_delete(self, id):
        self.__file_dao.file_delete(id)

    # 查看文件信息
    def file_view(self, id):
        result = self.__file_dao.file_view(id)
        return result