from flask import Blueprint, render_template, session, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.db import mysql

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods = ['GET', 'POST'])
def register():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        cur = mysql.connection.cursor()
    
        cur.execute("INSERT INTO users(name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    
        mysql.connection.commit()
        cur.close()
        
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth_bp.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()

        cur.execute("SELECT * FROM users WHERE email = (%s)", (email,))
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user[3], password):
            session["user_id"] = user[0]
            return redirect(url_for('applications.dashboard'))
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    redirect(url_for('auth.login'))
