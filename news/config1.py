import mysql.connector
try:
    config = {
        "host": "localhost",
        "port": "9002",
        "user": "root",
        "password": "12345678",
        "database": "demo"
    }
    con = mysql.connector.connect(**config)
    con.start_transaction()
    cursor = con.cursor()
    sql = "insert into t_emp (empno, ename, job, mgr, hiredate, sal, comm, deptno) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (9500, "赵娜", "SALESMAN", None, "1985-01-12", 2500, None, 10))
    for one in cursor:
        print(one)
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
finally:
    if "con" in dir():
        con.close()