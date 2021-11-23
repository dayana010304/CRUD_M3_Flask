# importar el archivo de la conexión a la BD
from configdb import get_connection

def add_user(email, name, passwd ):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO users (email, name, passwd) VALUES (%s,%s,%s)",(email, name, passwd))
    cnn.commit()
    cnn.close()

def get_user( email, passwd):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE email=%s and passwd =%s",(email, passwd))
    cnn.commit()
    cnn.close()

