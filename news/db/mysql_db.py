import mysql.connector.pooling
__config = {
    "host": "localhost",
    "port": "9002",
    "user": "root",
    "password": "12345678",
    "database": "vega"
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_size=10
    )
    # con = pool.get_connection()
    # cursor = con.cursor()
    # sql = "SELECT COUNT(*) FROM t_user u JOIN t_role r ON u.role_id = r.id " \
    #       "WHERE u.username = %s"
    # cursor.execute(sql, ('admin',))
    # for one in cursor:
    #     print(one)
except Exception as e:
    print(e)
finally:
    pass