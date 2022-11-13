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
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'
app.config['MYSQL_USER'] = 'sqluser'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'NFT_System'
mysql = MySQL(app)


CORS(app, support_credentials=True)

def get_current_data(from_sym='BTC', to_sym='USD', exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price'    
    
    parameters = {'fsym': from_sym,
                  'tsyms': to_sym }
    
    if exchange:
        parameters['e'] = exchange
        
    response = requests.get(url, params=parameters)   
    data = response.json()
    
    return data
ETH_value = get_current_data('ETH','USD','coinbase')
print(ETH_value['USD'])

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
        type = req['type']
        cursor = mysql.connection.cursor()
        if (type == 'trader'):
            cursor.execute("SELECT email, pass FROM TRADER WHERE email = % s AND pass = % s", (email, password, ))
        else:
            cursor.execute("SELECT Email, password FROM MANAGER WHERE Email = % s AND password = % s", (email, password, ))
        #rows = cursor.execute(query1)
        account = cursor.fetchone()
        if account:
            session['user_id'] = email
            token = jwt.encode({
                'user_id': session['user_id'],
                'exp': datetime.utcnow() + timedelta(hours=24)
            }, app.config['SECRET_KEY'])
            token = token.encode().decode('UTF-8')
            if(type == 'trader'):
                msg = 'Trader logged in Successfully'
            else:
                msg = 'Manager logged in Successfully'
            responseObject = {
                'status': 'success',
                'message': msg,
                'auth_token': token
            }
            return jsonify(responseObject), 200
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Incorrect Username or Password.'
            }
            return jsonify(responseObject), 401   

            
@cross_origin(origin='*',headers=['Content-Type','application/json'])
@app.route('/register', methods=['GET', 'POST'])
def register():
        msg = ''
        req = request.get_json()
        firstName = req['firstName']
        lastName = req['lastName']
        email = req['email']
        password = req['password']
        phone = req['phoneNumber']
        cell_phone = req['cellphoneNumber']
        phone = '+' + phone
        cell_phone = '+' + cell_phone
        check_phone = phonenumbers.parse(phone)
        city = req['city']
        trader_id = randN(10)
        state = req['state']
        street_address = req['streetAddress']
        zipcode = req['zipCode']
        cursor = mysql.connection.cursor()
        priv = secrets.token_hex(32)
        private_key = "0x" + priv
        acct = Account.from_key(private_key)
        cursor.execute('SELECT * FROM TRADER WHERE email = % s', (email,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !' 
        elif not re.match(r'[A-Za-z0-9]+', firstName):
            msg = 'Username must contain only characters and numbers !'
        elif (phonenumbers.is_possible_number(check_phone) == 'FALSE'):
            msg = 'Phone number is invalid !'
        elif not password or not email or not firstName or not lastName or not phone or not cell_phone or not city or not zipcode or not street_address or not state:
            msg = 'Please fill out the form !'
        else:
            cursor.execute("INSERT INTO TRADER (t_id, t_name, t_lastname, pass, fiat_amt, Ph_no, cell_no, email, mem_type, eth_add, eth_cnt) VALUES (% s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s)", (trader_id, firstName, lastName, password, 500.00, phone, cell_phone, email, 'SILVER', acct.address, 0))
            cursor.execute("INSERT INTO ADDRESS (t_id, city, state, st_add, zipcode) VALUES (% s,% s, % s, % s, % s)", (trader_id, city, state, street_address, zipcode))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
            responseObject = {
                'status': 'Success',
                'message': msg
            }
            return jsonify(responseObject), 200
        
        msg = 'Incorrect SignUp Details Entered'
        responseObject = {
            'status': 'fail',
            'message': msg
        }
        return jsonify(responseObject), 401

@cross_origin(origin='*',headers=['Content-Type','application/json'])
@app.route('/getnfts', methods=['GET', 'POST'])
def get_image_url():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT name, NFT_value, NFT_add, URL FROM NFT')
    rows = cursor.fetchall()
    if(rows != None):
        data = []
        for row in rows:
            data.append({
                'name': row[0],
                'NFT_value': row[1],
                'NFT_add' : row[2],
                'Image_URL' : row[3]
            })
        responseObject = {
            'status': 'Success',
            'message': data
        }
        return jsonify(responseObject), 200
    responseObject = {
        'status': 'fail',
        'message': 'No Data found'
    }
    return jsonify(responseObject), 401

@cross_origin(origin='*',headers=['Content-Type','application/json'])
@app.route('/getTTransDetails', methods=['GET', 'POST'])
def get_ttrans_details():
    req = request.get_json()
    if(req):
        trader_id = req['trader_id']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT nft_trans_id, t_value, t_date_time, status FROM NFT_TRANSACTION WHERE t_id = % s', (trader_id,))
        nft_trans = cursor.fetchall()
        cursor.execute('SELECT * FROM FIAT_TRANSACTIONS WHERE t_id = % s', (trader_id,))
        fiat_trans = cursor.fetchall()
    else:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT nft_trans_id, t_value, t_date_time, status FROM NFT_TRANSACTION')
        nft_trans = cursor.fetchall()
        cursor.execute('SELECT ft_id, amount, type FROM FIAT_TRANSACTIONS')
        fiat_trans = cursor.fetchall()
    if(nft_trans != None or fiat_trans != None):
        nft_data = []
        for row in nft_trans:
            nft_data.append({
                'nft_trans_id': row[0],
                't_value' : row[1],
                't_date_time' : row[2],
                'status' : row[3]
            })
        fiat_data = []
        for row1 in fiat_trans:
            fiat_data.append({
                'ft_id': row1[0],
                'amount': row1[1],
                'type' : row1[2]
            })
        responseObject = {
            'status': 'Success',
            'nft_trans': nft_data,
            'fiat_trans': fiat_data,
        }
        return jsonify(responseObject), 200
    responseObject = {
        'status': 'fail',
        'message': 'No Data found'
    }
    return jsonify(responseObject), 401

@cross_origin(origin='*',headers=['Content-Type','application/json'])
@app.route('/buynfts', methods=['GET', 'POST'])
def buynfts():
    msg = ''
    req = request.get_json()
    trader_id = req['trader_id']
    nft_id = req['nft_id']
    nft_value = req['nft_value']
    comm_type = req['comm_type']
    
    
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