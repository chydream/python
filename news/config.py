import mysql.connector
# con = mysql.connector.connect(
#     host="localhost",
#     port="9002",
#     user="root",
#     password="12345678",
#     database="demo"
# )
config = {
    "host": "localhost",
    "port": "9002",
    "user": "root",
    "password": "12345678",
    "database": "demo"
}
try:
    con = mysql.connector.connect(**config)
    con.start_transaction()
    cursor = con.cursor()
    # sql = "insert into t_emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    sql = "select * from t_emp"
    cursor.execute(sql)
    con.commit()
except Exception as e:
    con.rollback()
    print(e)
finally:
    if "con" in dir():
        con.close()
# cursor = con.cursor()
# username = "1 or 1=1"
# password = "1 or 1=1"
# sql = "select count(*) from t_user where username=" + username + " and aes_decrypt(unhex(password), 'helloworld')=" + password
# sql2 = "select count(*) from t_user where username=%s and aes_decrypt(unhex(password), 'helloworld')= %s"
# sql1 = "insert into t_emp(empno,ename) values(%s,%s)"
# cursor.execute(sql2, (username, password))
# print(cursor.fetchone()[0])
# print(cursor)
# for one in cursor:
#     print(one)

# connector 事务控制函数
# cursor.execute(sql, (9600, "赵娜", "SALESMAN", None, "1985-12-1", 2500, None, 10))
# con.start_transaction([事务隔离级别])
# con.commit()
# con.rollback()
# 异常处理
# try:
#     con = mysql.connector.connect(..config)
#     [con = start_transaction()]
# except Exception as e:
#     [con.rollback()]
#     print(e)
# finally:
#     if "con" in dir():
#         con.close()

# con.close()