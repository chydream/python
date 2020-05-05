from db.mysql_db import pool

class StaffDao:
    # 添加职工信息
    def staff_add(self, truename, email, sex, deptno, job, phone, address):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_staff (truename, email, sex, deptno, job, phone, address, create_time) " \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s,NOW())"
            cursor.execute(sql, (truename, email, sex, deptno, job, phone, address))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 获取职工信息列表分页
    def get_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT s.id,s.truename,s.email,s.sex,d.deptname FROM t_staff s " \
                  "JOIN t_dept d ON s.deptno = d.deptno " \
                  "ORDER BY s.create_time DESC " \
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
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_staff"
            cursor.execute(sql)
            result = cursor.fetchone()[0]
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 修改职工信息
    def staff_update(self, deptno, job, phone, address, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_staff SET deptno = %s,job = %s,phone = %s,address = %s WHERE id = %s"
            cursor.execute(sql, (deptno, job, phone, address, id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 删除职工
    def staff_delete(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_staff WHERE id = %s"
            cursor.execute(sql,(id,))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查看职工信息
    def staff_view(self, email):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT s.id,s.truename,s.email,s.sex,d.deptname FROM t_staff s " \
                  "JOIN t_dept d ON s.deptno = d.deptno " \
                  "WHERE email = %s " \
                  "ORDER BY s.create_time DESC "
            cursor.execute(sql, (email,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()