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
#print(ETH_value['USD'])

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
            cursor.execute("SELECT t_id, email, pass FROM TRADER WHERE email = % s AND pass = % s", (email, password, ))
        else:
            cursor.execute("SELECT M_id, Email, password FROM MANAGER WHERE Email = % s AND password = % s", (email, password, ))
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
                'auth_token': token,
                'id': account[0]
            }
            return jsonify(responseObject), 200
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Incorrect Username or Password.'
            }
            return jsonify(responseObject), 200   

            
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
                'status': 'success',
                'message': msg
            }
            return jsonify(responseObject), 200
        
        msg = 'Incorrect SignUp Details Entered'
        responseObject = {
            'status': 'fail',
            'message': msg
        }
        return jsonify(responseObject), 200

@cross_origin(origin='*',headers=['Content-Type','application/json'])
@app.route('/getnfts', methods=['GET', 'POST'])
def getnfts():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT name, NFT_value, NFT_add, URL FROM NFT WHERE t_id is NULL')
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
            'status': 'success',
            'message': data,
        }
        return jsonify(responseObject), 200
    responseObject = {
        'status': 'fail',
        'message': 'No Data found'
    }
    return jsonify(responseObject), 200

@cross_origin(origin='*',headers=['Content-Type','application/json'])
@app.route('/getTraderNfts', methods=['POST'])
def getTraderNfts():
    req = request.get_json()
    trader_id = req['id']
    now = datetime.now()
    toDate = now - timedelta(days = 30)
    total_fiat_amount = 0
    total_nft_value1 = 0
    total_nft_value = 0
    total_amt = 0
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT SUM(amount) FROM FIAT_TRANSACTIONS WHERE t_date_time >= %s and t_date_time <= %s and t_id = %s', (toDate, now, trader_id, ))
    total_fiat_amount = cursor.fetchone()
    
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT SUM(t_value) FROM NFT_TRANSACTION WHERE t_date_time >= %s and t_date_time <= %s and t_id = %s', (toDate, now, trader_id, ))
    total_nft_value1 = cursor.fetchone()
    if(total_nft_value1[0] != None):
        total_nft_value = total_nft_value1[0] * ETH_value['USD']
    if(total_fiat_amount[0] != None):
        total_amt = total_fiat_amount[0] + total_nft_value
    if(total_amt > 100000):
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE TRADER SET mem_type = %s WHERE t_id = %s", ('GOLD', trader_id, ))
        mysql.connection.commit()
    else:
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE TRADER SET mem_type = %s WHERE t_id = %s", ('SILVER', trader_id, ))
        mysql.connection.commit()
            
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT fiat_amt, eth_cnt FROM TRADER WHERE t_id = % s', (trader_id,))
    trader_transDetail = cursor.fetchone()
    cursor.execute('SELECT name, NFT_value, NFT_add, URL FROM NFT WHERE t_id = % s', (trader_id,))
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
            'status': 'success',
            'message': data,
            'fiatAmt' : trader_transDetail[0],
            'ethCnt' : trader_transDetail[1],
            'ethValue': ETH_value['USD']
        }
        return jsonify(responseObject), 200
    responseObject = {
        'status': 'fail',
        'message': 'No Data found'
    }
    return jsonify(responseObject), 200
       
@cross_origin(origin='*',headers=['Content-Type','application/json'])
@app.route('/getTTransHistory', methods=['GET', 'POST'])
def get_ttrans_history():
    req = request.get_json()
    trader_id = req['id']
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT nft_trans_id, name, t_value, t_date_time, status FROM NFT_TRANSACTION WHERE t_id = % s', (trader_id,))
    nft_trans = cursor.fetchall()
    cursor.execute('SELECT ft_id, amount, type, t_date_time FROM FIAT_TRANSACTIONS WHERE t_id = % s', (trader_id,))
    fiat_trans = cursor.fetchall()

    if(nft_trans != None or fiat_trans != None):
        nft_data = []
        for row in nft_trans:
            nft_data.append({
                'nft_trans_id': row[0],
                'name' : row[1],
                't_value' : row[2],
                't_date_time' : row[3],
                'status' : row[4]
            })
        fiat_data = []
        for row1 in fiat_trans:
            fiat_data.append({
                'ft_id': row1[0],
                'amount': row1[1],
                'type' : row1[2],
                'dateTime' : row1[3]
            })
        responseObject = {
            'status': 'success',
            'nft_trans': nft_data,
            'fiat_trans': fiat_data,
        }
        return jsonify(responseObject), 200
    responseObject = {
        'status': 'fail',
        'message': 'No Data found'
    }
    return jsonify(responseObject), 200

@cross_origin(origin='*',headers=['Content-Type','application/json'])
@app.route('/getAllTrader_TransHistory', methods=['GET', 'POST'])
def get_all_trader_trans_history():
    req = request.get_json()
    fromDate = req['from']
    toDate = req['to']
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT t_id, nft_trans_id, name, t_value, t_date_time, status, com_rate FROM NFT_TRANSACTION where t_date_time >= %s and t_date_time <= %s', (fromDate, toDate,))
    nft_trans = cursor.fetchall()
    cursor.execute('SELECT t_id, ft_id, amount, type, t_date_time FROM FIAT_TRANSACTIONS where t_date_time >= %s and t_date_time <= %s', (fromDate, toDate,))
    fiat_trans = cursor.fetchall()
    if(nft_trans != None or fiat_trans != None):
        nft_data = []
        for row in nft_trans:
            nft_data.append({
                't_id': row[0],
                'nft_trans_id': row[1],
                'name' : row[2],
                't_value' : row[3],
                't_date_time' : row[4],
                'status' : row[5],
                'com_rate' : row[6]
            })
        fiat_data = []
        for row1 in fiat_trans:
            fiat_data.append({
                't_id': row1[0],
                'ft_id': row1[1],
                'amount': row1[2],
                'type' : row1[3],
                'dateTime' : row1[4]
            })
        responseObject = {
            'status': 'success',
            'nft_trans': nft_data,
            'fiat_trans': fiat_data,
        }
        return jsonify(responseObject), 200
    responseObject = {
        'status': 'fail',
        'message': 'No Data found'
    }
    return jsonify(responseObject), 200

@cross_origin(origin='*',headers=['Content-Type','application/json'])
@app.route('/transaction', methods=['GET', 'POST'])
def addMoney():
    msg = ''
    req = request.get_json()
    trader_id = req['id']
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    amount = req['amount']
    type = req['type'] 
    ft_id = randN(10)
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT fiat_amt, eth_cnt FROM TRADER WHERE t_id = % s', (trader_id,))
    current_amt = cursor.fetchone()
    total_amt = int(current_amt[0]) + int(amount)
    total_eth = int(current_amt[1]) + int(amount)
    cursor.execute('SELECT * FROM TRADER WHERE t_id = % s', (trader_id,))
    row = cursor.fetchone()
    if row:
        if(type == 'USD'):
            cursor.execute("INSERT INTO FIAT_TRANSACTIONS (t_id, ft_id, t_date_time, amount, status, type) VALUES (% s, % s, % s, % s, % s, % s)", (trader_id, ft_id, date_time, amount, 'success', type))
            cursor.execute("UPDATE TRADER SET fiat_amt = %s WHERE t_id = %s", (total_amt, trader_id, ))
            mysql.connection.commit()
            msg = 'USD Successfully added to Wallet'
        else: 
            cursor.execute("INSERT INTO FIAT_TRANSACTIONS (t_id, ft_id, t_date_time, amount, status, type) VALUES (% s, % s, % s, % s, % s, % s)", (trader_id, ft_id, date_time, amount, 'success', type))
            cursor.execute("UPDATE TRADER SET eth_cnt = %s WHERE t_id = %s", (total_eth, trader_id, ))
            mysql.connection.commit()
            msg = 'ETH Successfully added to Wallet'
            
        responseObject = {
            'status': 'success',
            'message': msg
            }
        return jsonify(responseObject), 200
        
    msg = 'Some Error Occured while Entering the data'
    responseObject = {
        'status': 'fail',
        'message': msg
    }
    return jsonify(responseObject), 200

@cross_origin(origin='*',headers=['Content-Type','application/json'])
@app.route('/buynfts', methods=['GET', 'POST'])
def buynfts():
    msg = ''
    req = request.get_json()
    trader_id = req['id']
    nft_address = req['nftAdd']
    com_type = req['com_type']
    now = datetime.now()
    trans_id = randN(10)
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT mem_type, eth_cnt, fiat_amt, eth_add FROM TRADER WHERE t_id = % s', (trader_id,))
    mem_type = cursor.fetchone()
    cursor.execute('SELECT com_rate FROM CLASSIFICATION WHERE mem_id = % s', (mem_type[0],))
    com_rate = cursor.fetchone()
    cursor.execute('SELECT NFT_value, NFT_id, name, URL, sell_add, NFT_add FROM NFT WHERE NFT_add = % s', (nft_address,))
    nft_value = cursor.fetchone()
    if(mem_type[1] < nft_value[0]):
        msg = 'You dont have enough Eth to buy NFTs'
    else:    
        cursor = mysql.connection.cursor()
        remaining_nft_value = mem_type[1] - nft_value[0]
        cursor.execute("UPDATE TRADER SET eth_cnt = %s WHERE t_id = %s", (remaining_nft_value, trader_id, ))
        mysql.connection.commit()
    if(com_type == 'ETH'):
        comm1 = (ETH_value['USD']*nft_value[0]*com_rate[0])/100
        comm = comm1/ETH_value['USD']
        if(mem_type[1] >= comm): 
            remaining_eth_balance = mem_type[1] - comm
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE TRADER SET eth_cnt = %s WHERE t_id = %s", (remaining_eth_balance, trader_id, ))
            mysql.connection.commit()
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE NFT SET t_id = %s WHERE NFT_add = %s", (trader_id, nft_address, ))
            mysql.connection.commit()
            msg = 'Succesfully Bought the NFT'
        else:
            msg = 'You dont have enough ethereum Count to pay the commission'
    else:
        comm = (ETH_value['USD']*nft_value[0]*com_rate[0])/100
        if(mem_type[2] >= comm):   
            remaining_eth_balance = mem_type[2] - comm
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE TRADER SET fiat_amt = %s WHERE t_id = %s", (remaining_eth_balance, trader_id, ))
            mysql.connection.commit()
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE NFT SET t_id = %s WHERE NFT_add = %s", (trader_id, nft_address, ))
            mysql.connection.commit()
            msg = 'Succesfully Bought the NFT'
        else:
            msg = 'You dont have enough fiat amount to pay the commission'
    
    if(msg == 'You dont have enough Eth to buy NFTs' or msg == 'You dont have enough ethereum Count to pay the commission' or msg == 'You dont have enough fiat amount to pay the commission'):
        responseObject = {
            'status': 'fail',
            'message': msg
        }
        return jsonify(responseObject), 200
    else:
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO NFT_TRANSACTION (t_id ,NFT_id,name,t_date_time,com_rate,status,buyer_eth_add ,seller_eth_add, com_type, mem_type ,nft_add ,t_value,nft_trans_id ,URL) VALUES (% s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s)", (trader_id, nft_value[1], nft_value[2], now, com_rate, 'success', mem_type[3], nft_value[4], com_type, mem_type[0], nft_value[5], nft_value[0], trans_id, nft_value[3] ))
        mysql.connection.commit()
        responseObject = {
            'status': 'success',
            'message': msg
        }
        return jsonify(responseObject), 200

@cross_origin(origin='*',headers=['Content-Type','application/json'])
@app.route('/sellnfts', methods=['GET', 'POST'])
def sellnfts():
    msg = ''
    req = request.get_json()
    trader_id = req['trader_id']
    nft_address = req['nftAdd']
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT t_id FROM NFT WHERE NFT_add = % s', (nft_address,))
    t_id = cursor.fetchone()
    if(trader_id == t_id):
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT NFT_value FROM NFT WHERE NFT_add = % s', (nft_address,))
        nft_value = cursor.fetchone()
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT eth_add, eth_cnt FROM TRADER WHERE t_id = % s', (trader_id,))
        eth_add = cursor.fetchone()
        update_amt = nft_value + eth_add[1]
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE TRADER SET eth_cnt = %s WHERE t_id = %s", (update_amt, trader_id, ))
        mysql.connection.commit()
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE NFT SET t_id = %s and sell_add = %s WHERE NFT_add = %s", ('', eth_add, nft_address, ))
        mysql.connection.commit()
        msg = 'Successfully Sold the Eth'
        responseObject = {
            'status': 'success',
            'message': msg
        }
        return jsonify(responseObject), 200
    else: 
        msg = 'You dont own that NFT'
        responseObject = {
            'status': 'fail',
            'message': msg
        }
        return jsonify(responseObject), 200

@cross_origin(origin='*',headers=['Content-Type','application/json'])
@app.route('/cancel', methods=['GET', 'POST'])
def cancel():
    req = request.get_json()
    trader_id = req['id']
    toDate = datetime.now()
    fromDate = toDate - timedelta(minutes = 15)
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT nft_trans_id, name, t_value, t_date_time, status FROM NFT_TRANSACTION WHERE t_id = % s and t_date_time >= %s and t_date_time < %s and status = %s', (trader_id, fromDate, toDate,'success'))
    nft_trans = cursor.fetchall()
    cursor.execute('SELECT ft_id, amount, type, t_date_time FROM FIAT_TRANSACTIONS WHERE t_id = % s and t_date_time >= %s and t_date_time < %s and status = %s', (trader_id, fromDate, toDate, 'success'))
    fiat_trans = cursor.fetchall()
    
    if(nft_trans != None or fiat_trans != None):
        nft_data = []
        for row in nft_trans:
            nft_data.append({
                'nft_trans_id': row[0],
                'name' : row[1],
                't_value' : row[2],
                't_date_time' : row[3],
                'status' : row[4]
            })
        fiat_data = []
        for row1 in fiat_trans:
            fiat_data.append({
                'ft_id': row1[0],
                'amount': row1[1],
                'type' : row1[2],
                'dateTime' : row1[3]
            })
        responseObject = {
            'status': 'success',
            'nft_trans': nft_data,
            'fiat_trans': fiat_data,
        }
        return jsonify(responseObject), 200
    responseObject = {
        'status': 'fail',
        'message': 'No Data found'
    }
    return jsonify(responseObject), 200
 
@cross_origin(origin='*',headers=['Content-Type','application/json'])
@app.route('/cancelPayment', methods=['GET', 'POST'])
def cancelPayment():
    msg = ''
    req = request.get_json()
    trans_id = req['trans_id']
    trader_id = req['id']
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT ft_id FROM FIAT_TRANSACTIONS WHERE t_id = %s and ft_id = % s', (trader_id, trans_id, ))
    ft_id = cursor.fetchone()
    if(ft_id[0] == ''):
        trans_type = 'NFT'
    else:
        trans_type ='fiat'
    if(trans_type == 'fiat'):
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE FIAT_TRANSACTIONS SET status = %s WHERE ft_id = %s", ( 'fail', trans_id))
        mysql.connection.commit()
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT mem_type, eth_cnt, fiat_amt FROM TRADER WHERE t_id = % s', (trader_id,))
        mem_type = cursor.fetchone()
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT amount, type FROM FIAT_TRANSACTIONS WHERE t_id = % s', (trader_id,))
        amount = cursor.fetchone()
        if(amount[1] == 'ETH'):
            remaining_eth_balance = mem_type[1] - amount[0]
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE TRADER SET eth_cnt = %s WHERE t_id = %s", (remaining_eth_balance, trader_id, ))
            mysql.connection.commit()
        else:   
            remaining_eth_balance = mem_type[2] - amount[0]
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE TRADER SET fiat_amt = %s WHERE t_id = %s", (remaining_eth_balance, trader_id, ))
            mysql.connection.commit()          
    else:
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE NFT_TRANSACTION SET status = %s WHERE nft_trans_id = %s", ( 'FAIL', trans_id))
        mysql.connection.commit()
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT mem_type, eth_cnt, fiat_amt FROM TRADER WHERE t_id = % s', (trader_id,))
        mem_type = cursor.fetchone()
        cursor.execute('SELECT t_value, com_rate, com_type FROM NFT_TRANSACTION WHERE nft_trans_id = % s', (trans_id,))
        t_value = cursor.fetchone()
        cursor = mysql.connection.cursor()
        remaining_nft_value = mem_type[1] + t_value[0]
        cursor.execute("UPDATE TRADER SET eth_cnt = %s WHERE t_id = %s", (remaining_nft_value, trader_id, ))
        mysql.connection.commit() 

        if(t_value[2] == 'ETH'):
            comm1 = (ETH_value['USD']*t_value[0]*t_value[1])/100
            comm = comm1/ETH_value['USD']
            remaining_eth_balance = mem_type[1] + comm
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE TRADER SET eth_cnt = %s WHERE t_id = %s", (remaining_eth_balance, trader_id, ))
            mysql.connection.commit()
        else:
            comm = (ETH_value['USD']*t_value[0]*t_value[1])/100   
            remaining_eth_balance = mem_type[2] + comm
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE TRADER SET fiat_amt = %s WHERE t_id = %s", (remaining_eth_balance, trader_id, ))
            mysql.connection.commit()
            
        cursor = mysql.connection.cursor()  
        cursor.execute('SELECT nft_add FROM NFT_TRANSACTION WHERE nft_trans_id = % s', (trans_id,))
        nft_add = cursor.fetchone()
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE NFT SET t_id = %s WHERE NFT_add = %s", ('', nft_add[0], ))
        mysql.connection.commit()    
    
    msg = 'Successfully cancelled the Transaction.'
    responseObject = {
        'status': 'success',
        'message': msg
    }
    return jsonify(responseObject), 200
    
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