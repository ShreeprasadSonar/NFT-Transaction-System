from flask import Flask, render_template, request, session, redirect, url_for, g, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from eth_account import Account
import secrets
import re
import phonenumbers
import random
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'
app.config['MYSQL_USER'] = 'sqluser'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'NFT_System'
mysql = MySQL(app)

#Server_Session = Session(app)

CORS(app, support_credentials=True)

def randN(N):
	min = pow(10, N-1)
	max = pow(10, N) - 1
	return random.randint(min, max)

@app.before_request
def before_request():
    g.user = None
    
    if 'user_id' in session:
        query1 = "SELECT * from TRADER where email = '{un}'".format(un = session['user_id'])
        g.user = query1

@cross_origin(origin='*',headers=['Content-Type','application/json'])  
@app.route('/login', methods=['POST'])
def login():
        session.pop('user_id', None)
        msg = ''
        req = request.get_json()
        email = req['email']
        password = req['password']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT email, pass FROM TRADER WHERE email = % s AND pass = % s", (email, password, ))
        #rows = cursor.execute(query1)
        account = cursor.fetchone()
        if account:
            session['user_id'] = email
            token = jwt.encode({
                'user_id': session['user_id'],
                'exp': datetime.utcnow() + timedelta(hours=24)
            }, app.config['SECRET_KEY'])
            token = token.encode().decode('UTF-8')
            msg = 'Logged in Successfully'
            responseObject = {
                    'status': 'success',
                    'message': msg,
                    'auth_token': token
                }
            return jsonify(responseObject), 200
            #return render_template('dashboard.html', msg = msg)
        else:
            responseObject = {
                    'status': 'fail',
                    'message': 'Incorrect Username or Password.',
                }
            return jsonify(responseObject), 401   
            #return render_template('login.html', msg = msg)
   
@app.route('/register', methods=['POST'])
def register():
        msg = ''
        req = request.get_json()
        firstName = req['firstName']
        lastName = req['lastName']
        temp_name = firstName + lastName
        name = firstName + ' ' + lastName
        email = req['email']
        password = req['password']
        phone = req['phone']
        phone = '+' + phone
        check_phone = phonenumbers.parse(phone)
        cell_phone = req['cellphoneNumber']
        city = req['city']
        trader_id = randN(10)
        state = req.json['state']
        street_address = req['st_address']
        zipcode = req['zipcode']
        cursor = mysql.connection.cursor()
        priv = secrets.token_hex(32)
        private_key = "0x" + priv
        acct = Account.from_key(private_key)
        #print("Address:", acct.address)
        cursor.execute('SELECT * FROM TRADER WHERE email = % s', (email,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !' 
        elif not re.match(r'[A-Za-z0-9]+', temp_name):
            msg = 'Username must contain only characters and numbers !'
        elif (phonenumbers.is_possible_number(check_phone) == 'FALSE'):
            msg = 'Phone number is invalid !'
        elif not password or not email or not firstName or not lastName or not phone or not cell_phone or not city or not zipcode or not street_address or not state:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO TRADER (t_id, t_name, pass, fiat_amt, Ph_no, cell_no, email, mem_type, eth_add, eth_cnt) VALUES (%s, % s,% s, %s, % s, %s, %s, %s, %s, %s)', (trader_id, name, password, 40.25, phone, cell_phone, email, 'SILVER', acct.address, 0))
            cursor.execute('INSERT INTO ADDRESS (t_id, city, state, st_add, zipcode) VALUES (% s,% s, % s, %s, %s)', (trader_id, city, state, street_address, zipcode))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            #return jsonify({"Success":"SignUp Successful"}), 201
            return redirect(url_for('login'), msg = msg)
        #return jsonify({"Failed":"Incorrect Username or Password"}), 409
        return redirect(url_for('register'), msg = msg)

@app.route('/homepage', methods=['GET'])
def dashboard():
    if not g.user:
        return redirect(url_for('login')) 
    
    return render_template('homepage.html')

@app.route('/logout', methods=['POST'])
def logout(): 
    session.pop['user_id']
    return render_template('/')

if __name__ == '__main__':
    app.run(debug=True)