from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__) 

# variables of the connection in the database

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcontacts'

mysql = MySQL(app) 

# Settings of the session

app.secret_key = 'mysecretkey' 

# Routes of direcition for URL  

@app.route('/')
def Index():
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM contacts')
        data = cur.fetchall()
        return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
    
        #Operation INSERT
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        mysql.connection.commit()
        flash('Contact added with success!') 

        return redirect(url_for('Index'))

@app.route('/edit')
def edit_contact():
    return 'edit_contact'

@app.route('/delete')
def delete_contact():
    return 'delete_contact'

#Inicialize the server in port 3000

if __name__ == '__main__':
    app.run(port = 3000, debug = True)