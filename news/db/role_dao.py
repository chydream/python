from news.db.mysql_db import pool
class RoleDao:
    # 验证用户登录
    def search_list(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT id,role FROM t_role"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()