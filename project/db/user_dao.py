from db.mysql_db import pool

class UserDao:
    # 登录方法
    def login(self, username, password):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM t_user WHERE username = %s and AES_DECRYPT(UNHEX(password),'helloworld') = %s"
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            return True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 获取登录角色
    def search_user_role(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT  r.role " \
                  "FROM t_user u JOIN t_role r ON u.role_id = r.id " \
                  "WHERE u.username = %s"
            cursor.execute(sql, (username,))
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 获取用户id
    def get_userid(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT id FROM t_user WHERE username = %s"
            cursor.execute(sql, (username,))
            userid = cursor.fetchone()[0]
            return userid
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
