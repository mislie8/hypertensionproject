import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL
#from imblearn.combine import SMOTEENN
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'yannimonamour'

app.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
app.config['MYSQL_USER'] = 'bee0c3b95e7998'
app.config['MYSQL_PASSWORD'] = 'c6cd756e'
app.config['MYSQL_DB'] = 'heroku_95979b18166eb20'

mysql = MySQL(app)

# create tables
def create_tables():
    conn = MySQLdb.connect(host='us-cdbr-east-06.cleardb.net', user='bee0c3b95e7998', password='c6cd756e', database='heroku_95979b18166eb20')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE `tablelog` (`id` int(11) NOT NULL AUTO_INCREMENT,`username` varchar(50) NOT NULL,`password` varchar(255) NOT NULL,`email` varchar(100) NOT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3")
    conn.commit()
    conn.close()
model = pickle.load(open('model.pkl', 'rb'))
@app.route("/")

@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM tablelog WHERE username = % s AND password = % s', (username, password, ))
		log = cursor.fetchone()
		if log:
			session['loggedin'] = True
			session['id'] = log['id']
			session['username'] = log['username']
			msg = 'Logged in successfully !'
			return render_template('form.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))
@app.route('/about', methods =['GET', 'POST'])
def about():
   return render_template('about.html')
@app.route('/home', methods =['GET', 'POST'])
def home():
   return render_template('about.html')
@app.route('/home', methods =['GET', 'POST'])
def help():
   return render_template('help.html')


@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'password2' in request.form and 'email' in request.form :
		username = request.form['username']
		password = request.form['password']
		password2 = request.form['password2']
		email = request.form['email']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM tablelog WHERE username = % s OR email = % s', (username, email))
		log = cursor.fetchone()
		
		if log:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only letters and numbers !'
		elif not username or not password or not password2 or not email:
			msg = 'Please fill out the form !'
		elif (len(password)<8):
			msg = 'password should be minimum 8 characters.'
		elif not re.search("[a-z]", password):
			msg = 'Password must contain uppercase and lowercase letter'
		elif not re.search("[A-Z]", password):	
			msg = 'Password must contain at least one capital letter'
		elif not re.search("[0-9]", password):
			msg = 'Password must contain at least one number'
		elif not re.search("[!\#$%&/?@}]", password):
		#elif not re.search("[_@$]", password):
			msg = 'Password must contain a special character'
		elif request.form['password'] != request.form['password2']:
			msg=('Passwords don\'t match.')
		else:
			cursor.execute('INSERT INTO tablelog VALUES (NULL, % s, % s, % s)', (username, password, email, ))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)
# def hello():
#     return render_template('form.html')

@app.route("/predict", methods=['POST'])
def predict():

    age = int(request.form['age'])
    bmi = int(request.form['bmi'])
    sex = int(request.form['sex'])	
    smoker= int(request.form['smoker'])
    physactivity = int(request.form['physactivity'])
    fruits= int(request.form['fruits'])
    veggies= int(request.form['veggies'])
    alcohol= int(request.form['alcohol'])
    prediction = model.predict([[age, bmi, sex, smoker, physactivity, fruits, veggies, alcohol]])
    output = round(prediction[0], 2)

    if (prediction[0] == 0):
	    prediction = "Normal"
    else:
        prediction = "Abnormal - Please talk to your provider about your result"
    
    # preparing the report
    if (smoker == 0):
        smoker = 'non-smoker'
    else:
        smoker= 'smoker'
    if (sex == 0):
        sex = 'Female'
    else:
        sex= 'Male'
    if (physactivity == 1):
        physactivity= 'active'
    else:
        physactivity= 'not active'
    if (fruits == 1):
        fruits= 'fruits'
    else:
        fruits= 'no fruits'
    if (veggies == 1):
        veggies= 'veggies'
    else:
        veggies= 'no veggies'
    if (alcohol == 1):
        alcohol= 'alcohol'
    else:
        alcohol= 'no alcohol'
    if (age == 1):
        ag1 = '18-24 year-old'
    elif (age == 2):
        ag1 = '25-29 year-old'
    elif (age == 3):
        ag1 = '30-34 year-old'
    elif (age == 4 ):
        ag1 = '35-39 year old'
    elif (age == 5):
        ag1 = '40-44year-old'
    elif (age == 6):
        ag1 = '45-49 year-old'
    elif (age == 7):
        ag1 = '50-54 year-old'
    elif (age == 8):
        ag1 = '55-59 year-old'
    elif (age == 9):
        ag1 = '60-64 year-old'
    elif (age == 10):
        ag1 = '65-69 year-old'
    elif (age == 11):
        ag1 = '70-74 year-old'
    elif (age == 9):
        ag1 = '75-79 year-old'
    else:
        ag1 ='80 year old and older'

    return render_template('form.html', prediction_text=f'This is your report: Your age group is {ag1}, you are a {sex}, you are a {smoker}, you are {physactivity}, your diet contents {fruits}, {veggies}, {alcohol}, your body mass index is {bmi} kg/m². Your result is: {prediction}')



if __name__ == '__main__':
    app.run()