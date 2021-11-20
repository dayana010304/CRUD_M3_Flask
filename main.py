from os import curdir
import os
from flask import Flask, render_template, session,url_for,request,redirect, flash
from werkzeug.utils import secure_filename
import customer_controller
import invoice_controller
import user_controller

app = Flask(__name__)
app.secret_key ='wagh'
app.config['UPLOAD_FOLDER'] = 'static/img'

@app.route('/')
def index():
    return render_template('/login.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form ['email']
        passwd = request.form ['passwd']
        session ['email'] = email
        session ['passwd'] = passwd
    user = user_controller.get_user(email, passwd)
    return redirect(url_for('customer', user=user))

@app.route('/form_add_user')
def form_add_user():
    return render_template('add_user.html')

@app.route('/customer')
def customer():
    if session['email'] == 'email' and session ['passwd'] == 'passwd':
        customers = customer_controller.get_customers()
        return render_template('customer.html',customers= customers)
    else: 
        return redirect('/')

@app.route('/save_user', methods=['POST'])
def save_user():
    email = request.form['email']
    passwd = request.form['passwd']
    if user_controller.get_user(email, passwd): 
        email = request.form['email']
        name = request.form['name']
        passwd = request.form['passwd']
        user_controller.add_user(email, name, passwd)
    else:
        print ("error, el cliente no existe") 
    return redirect('/form_add_user')


@app.route('/form_add_customer')
def form_add_customer():
    return render_template('add_customer.html')

@app.route('/edit_customer/<int:id>')
def edit_customer(id):
    customer = customer_controller.get_customer_id(id)
    return render_template('edit_customer.html', customer=customer)

@app.route('/delete_customer', methods=["POST"])
def delete_customer():
    customer_controller.delete_customer(request.form["id"])
    return redirect("/index")

@app.route('/save_customer', methods=['POST'])
def save_customer():
    name = request.form['name']
    document = request.form['document']
    status = request.form['status']
    phone = request.form['phone']
    customer_controller.add_customer(name, document, status, phone)
    return redirect('/')

@app.route('/update_customer', methods=['POST'])
def update_customer():
    id = request.form['id']
    name = request.form['name']
    document = request.form['document']
    status = request.form['status']
    phone = request.form['phone']
    customer_controller.update_customer(name, document, status, phone, id)
    return redirect('/')

@app.route('/invoices')
def invoices():
    invoices = invoice_controller.get_invoices()
    return render_template('invoices.html',invoices=invoices)

@app.route('/form_add_invoice')
def form_add_invoice():
    return render_template('add_invoice.html')

@app.route('/save_invoice', methods=['POST'])
def save_invoice():
    document = request.form['document']
    if invoice_controller.get_customerInvoice_doc(document): 
        number = request.form['number']
        document = request.form['document']
        date = request.form['date']
        price = request.form['price']
        balance = request.form['balance']
        invoice_controller.add_invoice(number,document, date, price, balance)
    else:
        print ("error, el cliente no existe") 
    return redirect('/invoices')


@app.route('/edit_invoice/<int:id>')
def edit_invoice(id):
    invoice = invoice_controller.get_invoice_id(id)
    return render_template('edit_invoice.html', invoice=invoice)

@app.route('/update_invoice', methods=['POST'])
def update_invoice():
    id = request.form['id']
    number = request.form['number']
    document = request.form['document']
    date = request.form['date']
    price = request.form['price']
    balance = request.form['balance']
    invoice_controller.update_invoice(number, document,  date, price, balance, id)
    return redirect('/invoices')

@app.route('/delete_invoice', methods=["POST"])
def delete_invoice():
    invoice_controller.delete_invoice(request.form["id"])
    return redirect("/invoices")



if __name__ == "__main__":
    app.run(port = 4500, debug=True)