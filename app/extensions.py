from server_info import *
import mysql.connector

class MySQLDatabase:
    def get_db_connection() -> mysql.connector.connection_cext.CMySQLConnection:
        conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            port=PORT
        )
        return conn
    
    def close_connection(conn):
        conn.close()
