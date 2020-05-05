from db.mysql_db import pool

class DeptDao:
    # 获取部门列表
    def get_list(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT deptno,deptname FROM t_dept ORDER BY deptno"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()