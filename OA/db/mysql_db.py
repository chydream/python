import mysql.connector.pooling
__config = {
    "host": "localhost",
    "port": "9002",
    "user": "root",
    "password": "12345678",
    "database": "oa"
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_size=10
    )
except Exception as e:
    print(e)
finally:
    pass