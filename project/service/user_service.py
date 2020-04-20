from db.user_dao import UserDao

class UserService:
    __user_dao = UserDao()

    # 登录方法
    def login(self, username, password):
        result = self.__user_dao.login(username, password)
        return result