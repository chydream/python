from db.user_dao import UserDao

class UserService:
    __user_dao = UserDao()

    # 登录方法
    def login(self, username, password):
        result = self.__user_dao.login(username, password)
        return result

    # 获取登录角色
    def search_user_role(self, username):
        role = self.__user_dao.search_user_role(username)
        return role

    # 获取用户id
    def get_userid(self, username):
        userid = self.__user_dao.get_userid(username)
        return userid