# 数据库连接池 connection pool
# 预先创建出一些数据库连接，然后缓存起来，避免了程序语言反复创建和销毁连接昂贵代价
import mysql.connector.pooling
try:
    config = {
        "host": "localhost",
        "port": "9002",
        "user": "root",
        "password": "12345678",
        "database": "demo"
    }
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=10
    )
    con = pool.get_connection()
    con.start_transaction()
    cursor = con.cursor()
    sqlSelect = "select * from t_emp"
    sqlInsert = "insert into t_emp_new (empno, ename, job, mgr, hiredate, sal, comm, deptno) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    sqlUpdate = "UPDATE t_emp SET sal = sal + %s where deptno = %s"
    sqlDelete = "DELETE e,d FROM t_emp e JOIN t_dept d ON e.deptno = d.deptno WHERE d.deptno = 10"
    sqlDeleteTrun = "TRUNCATE TABLE t_emp"
    # cursor.execute(sqlUpdate, (200, 20))
    # cursor.execute(sqlDeleteTrun)
    # data = [[9500, "赵娜", "SALESMAN", None, "1985-01-12", 2500, None, 10],[9600, "李娜", "SALESMAN", None, "1985-01-12", 2500, None, 10]]
    # cursor.executemany(sqlInsert, data)   #反复执行一条sql语句
    # tableAdd = "CREATE TABLE IF NOT EXISTS t_emp_new AS (SELECT * FROM t_emp)"
    tableAddNew = "CREATE TABLE IF NOT EXISTS t_emp_new like t_emp"
    cursor.execute(tableAddNew)
    sqlDone = "SELECT e.empno, e.ename, e.job, e.mgr, e.hiredate, e.sal, e.comm, e.deptno FROM t_emp e JOIN  ((SELECT a.deptno " \
              "FROM (SELECT deptno,AVG(sal) avg FROM t_emp GROUP BY deptno) a JOIN (SELECT AVG(sal) avg FROM t_emp) b WHERE a.avg > b.avg)) c " \
              "WHERE e.deptno = c.deptno"
    cursor.execute(sqlDone)
    data = []
    # cursor.fetchone()
    # cursor.fetchall()
    # sql = "insert into t_emp_new select * from t_emp where deptno in (20,10)"
    for one in cursor:
        data.append(one)
    for item in data:
        cursor.execute(sqlInsert, item)
    # cursor.executemany(sqlInsert, data)
    con.commit()
except Exception as e:
    print(e)
    if "con" in dir():
        con.rollback()
finally:
    pass
