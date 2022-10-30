from flask import Flask, render_template, request, session, redirect, url_for, g
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
app.secret_key = 'ruerhejdncjcdgduhnjsncjxckd'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'mysql123'
app.config['MYSQL_DB'] = 'NFT_System'
cors = CORS(app, resources={r"/login": {"origins": "*"}})
CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'application/json'
app.config["DEBUG"] = True

mysql = MySQL(app)

@app.before_request
def before_request():
    g.user = None
    
    if 't_id' in session:
        query1 = "SELECT * from TRADER where t_id = '{un}'".format(un = session['user_id'])
        g.user = query1
        
@app.route('/login', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def login():
    if request.method == 'POST':
        #session.pop['t_id', None]
        return request.json['credentials']
        email = request.form['email']
        password = request.form['password']
        # cursor = mysql.connection.cursor()
        #query1 = "SELECT t_name, pass from TRADER where t_name = '{un}' AND pass = '{pw}'".format(un = email, pw = password)
        #rows = cursor.execute(query1)
        #rows = rows.fetchall()
        if (email == "admin@admin.com" and password == "admin"):
            #query2 = "SELECT t_id from TRADER where t_name = '{un}' AND pass = '{pw}'".format(un = email, pw = password)
            #session['t_id'] = query2
            return redirect(url_for('dashboard'))
        
        return redirect(url_for('login'))
    
    return render_template('login.html')  
   
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['Rusername']
        password = request.form['Rpassword']
        email = request.form['Remail']
        cursor = mysql.connection.cursor()
        query1 = "INSERT INTO TRADER VALUES ('{u}','{p}','{e}')".format(u = username, p = password, e = email)
        cursor.execute(query1)
        mysql.connection.commit()
        return redirect('/login')
    
    return render_template('Register.html')

@app.route('/dashboard')
def dashboard():
    if not g.user:
        return redirect(url_for('login')) 
    
    return render_template('dashboard.html')
    
app.run(host='0.0.0.0', port=4200, debug=True)