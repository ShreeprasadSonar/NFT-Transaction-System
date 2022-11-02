from flask import Flask, render_template, request, session, redirect, url_for, g, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from eth_account import Account
import secrets
import MySQLdb.cursors
import re

app = Flask(__name__)
app.secret_key = 'somesecretkeythatishouldknow'
app.config['MYSQL_USER'] = 'sqluser'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'NFT_System'
mysql = MySQL(app)

CORS(app, support_credentials=True)

priv = secrets.token_hex(32)
private_key = "0x" + priv
#print ("SAVE BUT DO NOT SHARE THIS:", private_key)
acct = Account.from_key(private_key)
print("Address:", acct.address)

@app.before_request
def before_request():
    g.user = None
    
    if 'user_id' in session:
        query1 = "SELECT * from TRADER where email = '{un}'".format(un = session['user_id'])
        g.user = query1

@cross_origin(origin='*',headers=['Content-Type','Authorization'])  
@app.route('/login', methods=['POST'])
def login():
        session.pop('user_id', None)
        msg = ''
        email = request.json['email']
        password = request.json['password']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT email, pass FROM TRADER WHERE email = % s AND pass = % s", (email, password, ))
        #rows = cursor.execute(query1)
        account = cursor.fetchone()
        if account:
            session['user_id'] = email
            msg = 'Logged in Successfully'
            #return jsonify({"Success":"Login Successful"}), 400
            return redirect(url_for('dashboard'), msg = msg)
        else:
            #return jsonify({"Failed":"Incorrect Username or Password"}), 409   
            return redirect(url_for('login'), msg = msg)
   
@app.route('/register', methods=['GET', 'POST'])
def register():
        msg - ''
        email = request.json['email']
        password = request.json['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM TRADER WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        #elif not re.match(r'[A-Za-z0-9]+', username):
            #msg = 'Username must contain only characters and numbers !'
        elif not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO TRADER VALUES (% s, % s)', (password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    
        return redirect(url_for('login'), msg = msg)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if not g.user:
        return redirect(url_for('login')) 
    
    return render_template('dashboard.html')

@app.route('/logout', methods=['POST'])
def logout(): 
    session.pop['user_id']
    return render_template('/')

if __name__ == '__main__':
    app.run(debug=True)