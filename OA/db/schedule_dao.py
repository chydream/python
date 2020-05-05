from db.mysql_db import pool

class ScheduleDao:
    # 添加日程信息
    def schedule_add(self, username, year, month, day, plan):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_schedule (username, year, month, day, plan) " \
                  "VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(sql, (username, year, month, day, plan))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 获取日程信息列表分页
    def get_list(self, page, username, role):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            if role == '普通用户':
                sql = "SELECT id, year, month, day, plan FROM t_schedule s " \
                      "WHERE username = %s " \
                      "ORDER BY year,month,day DESC " \
                      "LIMIT %s,%s"
                cursor.execute(sql, (username, (page - 1) * 10, 10))
                result = cursor.fetchall()
                return result
            else:
                sql = "SELECT id, year, month, day, plan FROM t_schedule s " \
                      "ORDER BY year,month,day DESC " \
                      "LIMIT %s,%s"
                cursor.execute(sql, ((page - 1) * 10, 10))
                result = cursor.fetchall()
                return result

        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 获取总页数
    def get_total_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_schedule"
            cursor.execute(sql)
            result = cursor.fetchone()[0]
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 修改日程信息
    def schedule_update(self, year, month, day, plan, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_schedule SET year = %s,month = %s,day = %s,plan = %s WHERE id = %s"
            cursor.execute(sql, (year, month, day, plan, id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 删除日程
    def schedule_delete(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_schedule WHERE id = %s"
            cursor.execute(sql,(id,))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查看日程信息
    def schedule_view(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT  year, month, day, plan FROM t_schedule " \
                  "WHERE id = %s " \
                  "ORDER BY year,month,day DESC "
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()