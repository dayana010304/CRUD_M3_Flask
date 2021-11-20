# importar el archivo de la conexión a la BD
from configdb import get_connection

def add_customer(name, document, status, phone ):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO customer (name, document, status, phone) VALUES (%s,%s,%s,%s)",(name, document, status, phone))
    cnn.commit()
    cnn.close()

def update_customer( name, document, status, phone, id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE customer SET name = %s, document = %s, status = %s, phone = %s WHERE id = %s",(name, document, status, phone, id))
    cnn.commit()
    cnn.close()

def delete_customer(id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("DELETE from customer where document not in (SELECT document from invoice)")
    cnn.commit()
    cnn.close()

def get_customers():
    cnn = get_connection()
    customer = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, document, status, phone FROM customer")
        customer = cursor.fetchall()
    cnn.close()
    return customer

def get_customer_id(id):
    cnn = get_connection()
    customer = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, document, status, phone FROM customer WHERE id = %s",(id))
        customer = cursor.fetchone()
    cnn.close
    return customer