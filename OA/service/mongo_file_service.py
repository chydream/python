from db.mongo_file_dao import MongoFileDao

class MongoFileService:
    __mongo_file_dao = MongoFileDao()

    # 插入文件
    def add_file(self, fileinfo):
        self.__mongo_file_dao.add_file(fileinfo)

    # 获取文件
    def get_file(self, id):
        result = self.__mongo_file_dao.get_file(id)
        return result

    # 删除文件
    def delete_file(self, id):
        self.__mongo_file_dao.delete_file(id)

    # 下载文件
    def download_file(self, id, new_path):
        self.__mongo_file_dao.download_file(id, new_path)

    # 获取文件id
    def get_file_id(self, fileinfo):
        result = self.__mongo_file_dao.get_file_id(fileinfo)
        return result