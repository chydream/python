from db.mysql_db import pool

class NoticeDao:
    # 添加通知公告信息
    def notice_add(self, username, title, content):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_notice (sender, title, content, sendtime) " \
                  "VALUES (%s,%s,%s,Now())"
            cursor.execute(sql, (username, title, content))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 获取通知公告信息列表分页
    def get_list(self, page, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT id, sender, title, content, sendtime FROM t_notice " \
                  "ORDER BY sendtime DESC " \
                  "LIMIT %s,%s"
            cursor.execute(sql, ((page-1)*10, 10))
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
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_notice"
            cursor.execute(sql)
            result = cursor.fetchone()[0]
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 修改通知公告信息
    def notice_update(self, username, title, content, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_notice SET sender = %s,title = %s,content = %s,sendtime = NOW() WHERE id = %s"
            cursor.execute(sql, (username, title, content, id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 删除通知公告
    def notice_delete(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_notice WHERE id = %s"
            cursor.execute(sql,(id,))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查看通知公告信息
    def notice_view(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT  sender, title, content, sendtime FROM t_notice " \
                  "WHERE id = %s " \
                  "ORDER BY sendtime DESC "
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()