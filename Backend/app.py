from flask import Flask, render_template, request, session, redirect, url_for, g, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from flask_session import Session
from eth_account import Account
import secrets

app = Flask(__name__)
app.secret_key = 'somesecretkeythatishouldknow'
app.config['MYSQL_USER'] = 'sqluser'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'NFT_System'
mysql = MySQL(app)

CORS(app, support_credentials=True)
Server_Session = Session(app)

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
        #session.pop('user_id', None)
        email = request.json['email']
        password = request.json['password']
        cursor = mysql.connection.cursor()
        query1 = "SELECT email, pass from TRADER where email = '{un}' AND pass = '{pw}'".format(un = email, pw = password)
        rows = cursor.execute(query1)
        rows = rows.fetchall()
        if (rows == 1):
            #query2 = "SELECT t_id from TRADER where email = '{un}' AND pass = '{pw}'".format(un = email, pw = password)
            session['user_id'] = email
            return redirect(url_for('dashboard'))
        
        return redirect(url_for('login'))
   
@app.route('/register', methods=['GET', 'POST'])
def register():
        email = request.json['Remail']
        password = request.json['Rpassword']
        cursor = mysql.connection.cursor()
        query1 = "INSERT INTO TRADER VALUES ('{e}','{p}')".format(e = email, p = password)
        rows = cursor.execute(query1)
        rows = rows.fetchall()
        if (rows == 1):
            return jsonify({"error":"User Already Exists"}), 409
        mysql.connection.commit()
    
        return redirect(url_for('login'))

@app.route('/dashboard')
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