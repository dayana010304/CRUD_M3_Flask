from configdb import get_connection

def add_invoice(number, document, date, price, balance ):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO invoice (number, document, date, price, balance) VALUES (%s,(select document from customer where document = %s),%s,%s,%s)",(number, document, date, price, balance))
    cnn.commit()
    cnn.close()

def update_invoice( number, document, date, price, balance, id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE invoice SET number = %s, document = %s, date = %s, price = %s, balance = %s WHERE id = %s",(number, document, date, price, balance, id))
    cnn.commit()
    cnn.close()

def delete_invoice(id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("DELETE FROM invoice WHERE balance = 0 AND id=%s", (id))
    cnn.commit()
    cnn.close()

def get_invoices():
    cnn = get_connection()
    invoices = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, document, number, date, price, balance FROM invoice")
        invoices = cursor.fetchall()
    cnn.close()
    return invoices

def get_invoice_id(id):
    cnn = get_connection()
    invoice = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, number, document, date, price, balance FROM invoice WHERE id = %s",(id))
        invoice = cursor.fetchone()
    cnn.close
    return invoice

def get_customerInvoice_doc(document):
    cnn = get_connection()
    invoice = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT document FROM customer WHERE document = %s",(document))
        invoice = cursor.fetchone()
    cnn.close
    return invoice