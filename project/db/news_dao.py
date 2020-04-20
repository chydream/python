from db.mysql_db import pool
class NewsDao:
    # 获取审批新闻列表
    def search_unreview_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id,n.title,u.username,t.type FROM " \
                  "t_news n JOIN t_user u ON n.editor_id = u.id " \
                  "JOIN t_type t ON n.type_id = t.id " \
                  "WHERE n.state = %s " \
                  "ORDER BY n.id DESC " \
                  "LIMIT %s, %s"
            # print(sql)
            cursor.execute(sql, ("待审批", (page - 1)*10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 获取审批新闻总页数
    def search_unreview_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news WHERE state = %s"
            cursor.execute(sql, ("待审批",))
            count_page = cursor.fetchone()[0]
            # print(count_page)
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 审批新闻
    def update(self, news_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_news SET state = %s WHERE id = %s"
            # print(sql)
            cursor.execute(sql, ("已审批", news_id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 获取新闻列表
    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id,n.title,u.username,t.type FROM " \
                  "t_news n JOIN t_user u ON n.editor_id = u.id " \
                  "JOIN t_type t ON n.type_id = t.id " \
                  "ORDER BY n.id DESC " \
                  "LIMIT %s, %s"
            # print(sql)
            cursor.execute(sql, ((page - 1) * 10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 获取新闻总页数
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news"
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            # print(count_page)
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 删除新闻
    def delete(self, news_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_news WHERE id = %s"
            cursor.execute(sql, (news_id,))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

# news_dao = NewsDao()
# news_dao.search_count_page()