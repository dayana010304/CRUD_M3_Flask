# librería para conexión a Mysql
import pymysql

# método para realizar la conexión a mysql
def get_connection():
    return pymysql.connect(host='localhost',user='root',password='', db='facturacion')