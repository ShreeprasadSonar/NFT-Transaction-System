from flask import Flask, render_template, request, session, redirect, url_for, g, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'ruerhejdncjcdgduhnjsncjxckd'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'mysql123'
app.config['MYSQL_DB'] = 'NFT_System'
CORS(app, support_credentials=True)
Server_Session = Session(app)
app.config["DEBUG"] = True

mysql = MySQL(app)

@app.before_request
def before_request():
    g.user = None
    
    if 'user_id' in session:
        query1 = "SELECT * from TRADER where t_id = '{un}'".format(un = session['user_id'])
        g.user = query1

@cross_origin(origin='*',headers=['Content-Type','Authorization'])        
@app.route('/login', methods=['GET', 'POST'])
def login():
        session.pop['user_id', None]
        email = request.json['email']
        password = request.json['password']
        cursor = mysql.connection.cursor()
        query1 = "SELECT t_name, pass from TRADER where t_name = '{un}' AND pass = '{pw}'".format(un = email, pw = password)
        rows = cursor.execute(query1)
        rows = rows.fetchall()
        if (rows == 1):
            #session['token_id'] = token_id
            query2 = "SELECT t_id from TRADER where t_name = '{un}' AND pass = '{pw}'".format(un = email, pw = password)
            session['user_id'] = query2
            return redirect(url_for('dashboard'))
        
        return redirect(url_for('login'))  
   
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.json['Remail']
        password = request.json['Rpassword']
        cursor = mysql.connection.cursor()
        query1 = "INSERT INTO TRADER VALUES ('{e}','{p}')".format(e = email, p = password)
        rows = cursor.execute(query1)
        rows = rows.fetchall()
        if (rows == 1):
            return jsonify({"error":"User Already Exists"}), 409
        mysql.connection.commit()
        return redirect('/login')
    
    return jsonify({"error":"Unauthorised"}), 401

@app.route('/dashboard')
def dashboard():
    if not g.user:
        return redirect(url_for('login')) 
    
    return render_template('dashboard.html')
    
app.run(host='0.0.0.0', port=8000, debug=True)