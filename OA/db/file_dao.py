from db.mysql_db import pool

class FileDao:
    # 添加文件信息
    def file_add(self, username, filename, filesize, fileinfo, file_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_file (fileuploader, filename, filesize, fileinfo, fileuptime, fileid) " \
                  "VALUES (%s,%s,%s,%s,Now(),%s)"
            cursor.execute(sql, (username, filename, filesize, fileinfo, file_id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 获取文件信息列表分页
    def get_list(self, page, username, role):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            if role == "普通用户":
                sql = "SELECT id, fileid, fileuploader, filename, filesize, fileinfo, fileuptime FROM t_file " \
                      "WHERE fileuploader = %s " \
                      "ORDER BY fileuptime DESC " \
                      "LIMIT %s,%s"
                cursor.execute(sql, (username, (page - 1) * 10, 10))
                result = cursor.fetchall()
                return result
            else:
                sql = "SELECT id, fileid, fileuploader, filename, filesize, fileinfo, fileuptime FROM t_file " \
                      "ORDER BY fileuptime DESC " \
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
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_file"
            cursor.execute(sql)
            result = cursor.fetchone()[0]
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 修改文件信息
    def file_update(self, username, filename, filesize, fileinfo, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_file SET fileuploader = %s,filename = %s,filesize = %s,fileinfo = %s,fileuptime = NOW() WHERE id = %s"
            cursor.execute(sql, (username, filename, filesize, fileinfo, id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 删除文件
    def file_delete(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_file WHERE id = %s"
            cursor.execute(sql,(id,))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查看文件信息
    def file_view(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT  fileuploader, filename, filesize, fileinfo, fileuptime FROM t_file " \
                  "WHERE id = %s " \
                  "ORDER BY fileuptime DESC "
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()